import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.models.experience import ExperienceCost
from wfrp.character.views.create_character.spells import SpellsViews


@view_defaults(route_name="experience-talent")
class ExperienceTalentViews(SpellsViews):
    @view_config(renderer="wfrp.character:templates/forms/experience.pt")
    def form_view(self):
        schema = self.schema()
        form = deform.Form(schema, buttons=("Choose Spells",))
        if "Choose_Spells" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                talent = "Petty Magic"
                petty_spells = [
                    spell for spell, selected in captured["spells"].items() if selected
                ]
                self.character.spells = {"petty": petty_spells}
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
                spells_string = ", ".join(petty_spells)
                message = f"You have learned {talent} and the spells {spells_string}"
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
