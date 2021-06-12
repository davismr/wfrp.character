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
        schema = colander.SchemaNode(
            colander.Mapping(),
            title="Career Skills and Talents",
        )
        attribute_schema = colander.SchemaNode(
            colander.Mapping(),
            title="Attributes",
            description="Accept these results and gain 50XP. ",
        )
        for attribute in data["base_attributes"]:
            attribute_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    validator=True,
                    missing="",
                    widget=deform.widget.TextInputWidget(readonly=True),
                    name=attribute,
                )
            )
        schema.add(attribute_schema)
        return schema

    @view_config(renderer=__name__ + ":../templates/attributes.pt")
    def form_view(self):
        data = self.initialise_form()
        schema = self.schema(data)
        # TODO must be a better way to do this
        values = {"": {}}
        for attribute in ATTRIBUTES:
            values[""][attribute] = data["base_attributes"][attribute]
        form = deform.Form(
            schema,
            buttons=("Accept Attributes",),
            appstruct=values,
        )
        # TODO need 3 extra buttons
        # rearrange the results for 25XP
        # roll again for no XP
        # allocate 100 points across your attributes for no XP. Your attribute total is
        if "Accept_Attributes" in self.request.POST:
            try:
                form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                self.character.experience += 50
                for attribute in ATTRIBUTES:
                    value = int(data["base_attributes"][attribute])
                    value += data["bonus_attributes"][attribute]
                    attribute_lower = attribute.lower().replace(" ", "_")
                    setattr(self.character, attribute_lower, value)
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
