import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.utils import roll_2d10
from wfrp.character.views.base_view import BaseView

ATTRIBUTES = [
    "Weapon Skill",
    "Ballistic Skill",
    "Strength",
    "Toughness",
    "Initiative",
    "Agility",
    "Dexterity",
    "Intelligence",
    "Willpower",
    "Fellowship",
]

ATTRIBUTES_LOWER = [x.lower().replace(" ", "_") for x in ATTRIBUTES]


@view_defaults(route_name="attributes")
class AttributesViews(BaseView):
    def _roll_base_attributes(self):
        attributes = {}
        for attribute in ATTRIBUTES:
            attributes[attribute] = roll_2d10()
        return attributes

    def _get_bonus_attributes(self, species):
        attributes = {}
        for attribute in ATTRIBUTES:
            attributes[attribute] = 20
        if species == "Human":
            pass
        elif species == "Halfling":
            attributes["Weapon Skill"] += -10
            attributes["Ballistic Skill"] += 10
            attributes["Strength"] += -10
            attributes["Dexterity"] += -10
            attributes["Willpower"] += -10
            attributes["Fellowship"] += -10
        elif species == "Dwarf":
            attributes["Weapon Skill"] += 10
            attributes["Toughness"] += 10
            attributes["Agility"] += -10
            attributes["Dexterity"] += 10
            attributes["Willpower"] += 20
            attributes["Fellowship"] += -10
        elif species in ["High Elf", "Wood Elf"]:
            attributes["Weapon Skill"] += 10
            attributes["Ballistic Skill"] += 10
            attributes["Initiative"] += 20
            attributes["Agility"] += 10
            attributes["Dexterity"] += 10
            attributes["Intelligence"] += 10
            attributes["Willpower"] += 10
        else:
            raise NotImplementedError(f"{species} is not defined for bonus attributes")
        return attributes

    def initialise_form(self):
        if self.character.status["attributes"]:
            base_attributes = self.character.status["attributes"]
        else:
            base_attributes = self._roll_base_attributes()
            self.character.status = {"attributes": base_attributes}
        bonus_attributes = self._get_bonus_attributes(self.character.species)
        total_attributes = 0
        for attribute in base_attributes:
            total_attributes += base_attributes[attribute]
        return {
            "base_attributes": base_attributes,
            "bonus_attributes": bonus_attributes,
            "total_attributes": total_attributes,
        }

    def schema(self, data):
        species = self.character.species
        schema = colander.SchemaNode(
            colander.Mapping(),
            title="Character Attributes",
        )
        attribute_schema = colander.SchemaNode(
            colander.Mapping(),
            name="attributes",
            description=(
                "Accept these results and gain 50XP, or rearrange them for 25XP."
            ),
            validator=self.validate,
        )
        choices = []
        for attribute in data["base_attributes"]:
            choices.append(
                (
                    f"{attribute}_{data['base_attributes'][attribute]}",
                    f"{data['base_attributes'][attribute]} ({attribute})",
                )
            )
        for attribute in data["base_attributes"]:
            attribute_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    name=attribute,
                    description=(
                        f"{species} bonus is +{data['bonus_attributes'][attribute]}"
                    ),
                    widget=deform.widget.SelectWidget(values=choices),
                    validator=colander.OneOf([x[0] for x in choices]),
                    default=f"{attribute}_{data['base_attributes'][attribute]}",
                )
            )
        schema.add(attribute_schema)
        return schema

    def validate(self, form, values):
        used = list(values.values())
        duplicates = []
        while used:
            item = used.pop(0)
            if item in used:
                duplicates.append(f"{item.split('_')[1]} ({item.split('_')[0]})")
        if duplicates:
            raise colander.Invalid(
                form, f"You have used {', '.join(duplicates)} more than once"
            )

    @view_config(renderer="wfrp.character:templates/attributes.pt")
    def form_view(self):
        data = self.initialise_form()
        schema = self.schema(data)
        form = deform.Form(
            schema,
            buttons=("Accept Attributes",),
        )
        # TODO need 3 extra buttons
        # roll again for no XP
        # allocate 100 points across your attributes for no XP. Your attribute total is
        if "Accept_Attributes" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                matched = True
                for attribute in captured["attributes"]:
                    if attribute not in captured["attributes"][attribute]:
                        matched = False
                    value = int(captured["attributes"][attribute].split("_")[1])
                    value += data["bonus_attributes"][attribute]
                    attribute_lower = f'{attribute.lower().replace(" ", "_")}_initial'
                    setattr(self.character, attribute_lower, value)
                if matched:
                    self.character.experience += 50
                else:
                    self.character.experience += 25
                url = self.request.route_url("advances", uuid=self.character.uuid)
                self.character.status = {"advances": ""}
                return HTTPFound(location=url)
        else:
            html = form.render()

        static_assets = self.get_widget_resources(form)
        return {
            "form": html,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }
