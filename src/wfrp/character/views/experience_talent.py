import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPUnauthorized
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.magic.chanty import CHANTY_DATA
from wfrp.character.data.magic.miracles import get_miracles
from wfrp.character.models.experience import ExperienceCost
from wfrp.character.views.create_character.spells import SpellsViews


@view_defaults(route_name="experience-talent")
class ExperienceTalentViews(SpellsViews):
    def chanty_schema(self):
        schema = colander.SchemaNode(colander.Mapping(), title="Chanties")
        chanty_schema = colander.SchemaNode(
            colander.Mapping(),
            name="chanty",
            description="Select one chanty",
        )
        choices = [(x, x) for x in CHANTY_DATA]
        chanty_schema.add(
            colander.SchemaNode(
                colander.String(),
                widget=deform.widget.RadioChoiceWidget(values=choices),
                name="chanty",
            )
        )
        schema.add(chanty_schema)
        return schema

    def invoke_schema(self):
        schema = colander.SchemaNode(colander.Mapping(), title="Miracles")
        miracle_schema = colander.SchemaNode(
            colander.Mapping(),
            name="miracles",
            description="Select one miracle",
        )
        miracles = get_miracles(self.religion)
        choices = [(x, x) for x in miracles]
        miracle_schema.add(
            colander.SchemaNode(
                colander.String(),
                widget=deform.widget.RadioChoiceWidget(values=choices),
                name="miracle",
            )
        )
        schema.add(miracle_schema)
        return schema

    @view_config(renderer="wfrp.character:templates/forms/experience.pt")
    def form_view(self):  # noqa: C901
        talent = self.request.GET.get("talent")
        if talent == "Chanty":
            schema = self.chanty_schema()
            form = deform.Form(schema, buttons=("Choose Chanty",))
        elif talent == "Petty Magic":
            schema = self.schema()
            form = deform.Form(schema, buttons=("Choose Spells",))
        elif talent.startswith("Invoke ("):
            self.religion = talent.split(" (")[1].replace(")", "")
            schema = self.invoke_schema()
            form = deform.Form(schema, buttons=("Choose Miracles",))
        else:
            raise HTTPUnauthorized
        if (
            "Choose_Chanty" in self.request.POST
            or "Choose_Spells" in self.request.POST
            or "Choose_Miracles" in self.request.POST
        ):
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                if "Choose_Chanty" in self.request.POST:
                    talent = "Chanty"
                    chanty = captured["chanty"]["chanty"]
                    self.character.chanties = [chanty]
                    message = f"You have learned {talent} and the song {chanty}"
                elif "Choose_Spells" in self.request.POST:
                    talent = "Petty Magic"
                    petty_spells = []
                    for spell in captured["spells"]:
                        if captured["spells"][spell]:
                            petty_spells.append(spell)
                    self.character.petty_magic = petty_spells
                    spells_string = ", ".join(petty_spells)
                    message = (
                        f"You have learned {talent} and the spells {spells_string}"
                    )
                elif "Choose_Miracles" in self.request.POST:
                    talent = f"Invoke ({self.religion})"
                    miracle = captured["miracles"]["miracle"]
                    self.character.miracles = [miracle]
                    message = f"You have learned Invoke and the miracle {miracle}"
                self.character.talents[talent] = 1
                cost = self.character.cost_talent(self.character.talents[talent])
                experience_cost = ExperienceCost(
                    character_id=self.character.id,
                    type="talent",
                    cost=cost,
                    name=talent,
                )
                self.request.dbsession.add(experience_cost)
                self.character.experience -= cost
                self.character.experience_spent += cost
                self.request.session.flash(message, "success")
                url = self.request.route_url("experience", id=self.character.id)
                return HTTPFound(location=url)
        else:
            html = form.render()
        static_assets = form.get_widget_resources()
        return {
            "form": html,
            "character": self.character,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }
