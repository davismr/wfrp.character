import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.utils import roll_2d10
from wfrp.character.views.create_character.base_create import BaseCreateView

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


@view_defaults(
    renderer="wfrp.character:templates/forms/base_form.pt",
    permission="create_character",
)
class AttributesViews(BaseCreateView):
    def _roll_base_attributes(self):
        attributes = {}
        for attribute in ATTRIBUTES:
            attributes[attribute] = roll_2d10()
        return attributes

    def _get_bonus_attributes(self, species):
        attributes = {}
        for attribute in ATTRIBUTES:
            attributes[attribute] = 20
        if species.startswith("Human"):
            pass
        elif species == "Halfling":
            attributes["Weapon Skill"] += -10
            attributes["Ballistic Skill"] += 10
            attributes["Strength"] += -10
            attributes["Dexterity"] += -10
            attributes["Willpower"] += -10
            attributes["Fellowship"] += -10
        elif species in ["Dwarf", "Dwarf (Norse)"]:
            attributes["Weapon Skill"] += 10
            attributes["Toughness"] += 10
            attributes["Agility"] += -10
            attributes["Dexterity"] += 10
            attributes["Willpower"] += 20
            attributes["Fellowship"] += -10
        elif species == "Gnome":
            attributes["Ballistic Skill"] += -10
            attributes["Strength"] += -10
            attributes["Toughness"] += -5
            attributes["Initiative"] += 10
            attributes["Agility"] += 10
            attributes["Dexterity"] += 10
            attributes["Intelligence"] += 10
            attributes["Willpower"] += 20
            attributes["Fellowship"] += -5
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
            if "stage" in self.character.status:
                self.character.status = {
                    "attributes": base_attributes,
                    "stage": self.character.status["stage"],
                }
            else:
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

    def schema_initial(self, data):
        attribute_list = "-".join(
            [str(x) for x in sorted(data["base_attributes"].values())]
        )
        form_description = (
            "You can accept these results for +50XP, or rearrange them for +25XP, or "
            "reroll once for no extra XP. Alternatively, you can allocate 100 points "
            "across your 10 attributes."
        )
        species = self.character.species
        schema = colander.SchemaNode(
            colander.Mapping(),
            name="character_attributes",
            description=form_description,
        )
        attribute_schema = colander.SchemaNode(
            colander.Mapping(),
            name="attributes",
            description=(
                f"Rolled attributes are: {attribute_list}. Total rolled is "
                f"{data['total_attributes']}"
            ),
        )
        for attribute in data["base_attributes"]:
            attribute_schema.add(
                colander.SchemaNode(
                    colander.Integer(),
                    name=attribute,
                    description=(
                        f"Roll was {data['base_attributes'][attribute]} and {species} "
                        f"bonus is +{data['bonus_attributes'][attribute]}"
                    ),
                    widget=deform.widget.TextInputWidget(readonly=True),
                    default=(
                        data["base_attributes"][attribute]
                        + data["bonus_attributes"][attribute]
                    ),
                    missing=0,
                )
            )
        schema.add(attribute_schema)
        return schema

    def arrange_schema(self, data):
        attribute_list = "-".join(
            [str(x) for x in sorted(data["base_attributes"].values())]
        )
        choices = [(0, "Select")]
        for attribute in sorted(
            data["base_attributes"], key=data["base_attributes"].get
        ):
            choices.append(
                (
                    data["base_attributes"][attribute],
                    data["base_attributes"][attribute],
                )
            )
        if self.character.status["stage"] == "rearrange":
            form_description = (
                "Rearrange the ten rolls, assigning each to a different attribute for "
                "+25XP, or reroll once for no extra XP, and you will be able to "
                "rearrange across your attributes. Alternatively, you can allocate 100 "
                "points across your 10 attributes."
            )
        else:
            form_description = (
                "Rearrange the ten rolls, assigning each to a different attribute"
            )
        species = self.character.species
        schema = colander.SchemaNode(
            colander.Mapping(),
            name="character_attributes",
            description=(
                f"Rolled attributes are: {attribute_list}. Total rolled is "
                f"{data['total_attributes']}"
            ),
            validator=self.validate_arrange,
        )
        attribute_schema = colander.SchemaNode(
            colander.Mapping(),
            name="attributes",
            description=form_description,
        )
        for attribute in data["base_attributes"]:
            attribute_schema.add(
                colander.SchemaNode(
                    colander.Integer(),
                    name=attribute,
                    description=(
                        f"{species} bonus is +{data['bonus_attributes'][attribute]}"
                    ),
                    widget=deform.widget.SelectWidget(values=choices),
                    validator=colander.OneOf(data["base_attributes"].values()),
                )
            )
        schema.add(attribute_schema)
        return schema

    def validate_arrange(self, form, values):
        used = list(values["attributes"].values())
        not_used = list(self.character.status["attributes"].values())
        duplicates = []
        while used:
            item = used.pop(0)
            try:
                not_used.remove(item)
            except ValueError:
                duplicates.append(str(item))
        if duplicates:
            raise colander.Invalid(
                form,
                f"You have used {' and '.join(duplicates)} too many times "
                f"and not used {' or '.join([str(x) for x in not_used])}",
            )

    def schema_allocate(self, data):
        species = self.character.species
        schema = colander.SchemaNode(
            colander.Mapping(),
            title="Character Attributes",
        )
        attribute_schema = colander.SchemaNode(
            colander.Mapping(),
            name="attributes",
            description=(
                "Allocate 100 points across the 10 Characteristics as you prefer, with "
                "a minimum of 4 and a maximum of 18 allocated to any single "
                "Characteristic"
            ),
            validator=self.validate_allocate,
        )
        for attribute in ATTRIBUTES:
            attribute_schema.add(
                colander.SchemaNode(
                    colander.Integer(),
                    name=attribute,
                    description=(
                        f"{species} bonus is +{data['bonus_attributes'][attribute]}"
                    ),
                    widget=deform.widget.TextInputWidget(),
                    validator=self.validate_allocate_field,
                )
            )
        schema.add(attribute_schema)
        return schema

    def validate_allocate_field(self, form, values):
        if int(values) < 4:
            raise colander.Invalid(
                form,
                "Must be a minimum of 4",
            )
        elif int(values) > 18:
            raise colander.Invalid(
                form,
                "Must be a maximum of 18",
            )

    def validate_allocate(self, form, values):
        total = 0
        for value in values.values():
            total += int(value)
        if total != 100:
            raise colander.Invalid(
                form,
                f"Total must be 100, total is currently {total}",
            )

    def setup_form(self):
        buttons = []
        try:
            stage = self.character.status["stage"]
        except KeyError:
            stage = "initial"
        data = self.initialise_form()
        buttons.append("Accept Attributes")
        if stage == "initial":
            schema = self.schema_initial(data)
            buttons.append("Rearrange Attributes")
        if stage in ["initial", "rearrange"]:
            buttons.append("Reroll Attributes")
            buttons.append("Allocate Attributes")
        if stage in ["rearrange", "reroll"]:
            schema = self.arrange_schema(data)
        if stage == "allocate":
            schema = self.schema_allocate(data)
        form = deform.Form(
            schema,
            buttons=buttons,
        )
        return data, form

    @view_config(route_name="attributes")
    def form_view(self):
        if "Rearrange_Attributes" in self.request.POST:
            self.character.status = {
                "attributes": self.character.status["attributes"],
                "stage": "rearrange",
            }
        elif "Reroll_Attributes" in self.request.POST:
            attributes = self._roll_base_attributes()
            self.character.status = {"attributes": attributes, "stage": "reroll"}
        elif "Allocate_Attributes" in self.request.POST:
            self.character.status = {"attributes": None, "stage": "allocate"}
        data, form = self.setup_form()
        if "Accept_Attributes" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                self.update_values(captured)
                url = self.request.route_url("advances", id=self.character.id)
                self.character.status = {"advances": ""}
                return HTTPFound(location=url)
        else:
            html = form.render()
        static_assets = self.get_widget_resources(form)
        return {
            "form": html,
            "character": self.character,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }

    def update_values(self, captured):
        bonus_attributes = self._get_bonus_attributes(self.character.species)
        if "stage" not in self.character.status:
            # get base attributes from status initial form has calculated values
            base_attributes = self.character.status["attributes"]
        else:
            base_attributes = captured["attributes"]
        for attribute in ATTRIBUTES:
            field_name = f'{attribute.lower().replace(" ", "_")}_initial'
            value = int(base_attributes[attribute]) + bonus_attributes[attribute]
            setattr(self.character, field_name, value)
        if "stage" not in self.character.status:
            self.character.experience += 50
        elif self.character.status["stage"] == "rearrange":
            self.character.experience += 25
