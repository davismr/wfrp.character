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
        elif "choose" in self.character.status:
            base_attributes = []
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

    def _reroll(self):
        if "reroll" not in self.character.status:
            attributes = self._roll_base_attributes()
            self.character.status = {"attributes": attributes, "reroll": True}

    def schema(self, data):
        attribute_list = "-".join(
            [str(x) for x in sorted(data["base_attributes"].values())]
        )
        form_description = (
            f"Rolled attributes are: {attribute_list}. Total rolled is "
            f"{data['total_attributes']}"
        )
        species = self.character.species
        schema = colander.SchemaNode(
            colander.Mapping(),
            title="Character Attributes",
            description=form_description,
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
        for attribute in sorted(
            data["base_attributes"], key=data["base_attributes"].get
        ):
            choices.append(
                (
                    str(data["base_attributes"][attribute]),
                    str(data["base_attributes"][attribute]),
                )
            )
        for attribute in data["base_attributes"]:
            attribute_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    name=attribute,
                    description=(
                        f"Rolled was {data['base_attributes'][attribute]} and {species}"
                        f" bonus is +{data['bonus_attributes'][attribute]}"
                    ),
                    widget=deform.widget.SelectWidget(values=choices),
                    validator=colander.OneOf([x[0] for x in choices]),
                    default=str(data["base_attributes"][attribute]),
                )
            )
        schema.add(attribute_schema)
        return schema

    def validate(self, form, values):
        used = list(values.values())
        not_used = [str(x) for x in self.character.status["attributes"].values()]
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
                f"and not used {' or '.join(not_used)}",
            )

    def choose_schema(self, data):
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
            validator=self.choose_validate,
        )
        for attribute in ATTRIBUTES:
            attribute_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    name=attribute,
                    description=(
                        f"{species} bonus is +{data['bonus_attributes'][attribute]}"
                    ),
                    widget=deform.widget.TextInputWidget(),
                    validator=self.validate_choose_field,
                )
            )
        schema.add(attribute_schema)
        return schema

    def validate_choose_field(self, form, values):
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

    def choose_validate(self, form, values):
        total = 0
        for value in values.values():
            total += int(value)
        if total != 100:
            raise colander.Invalid(
                form,
                f"Total must be 100, total is currently {total}",
            )

    @view_config(renderer="wfrp.character:templates/attributes.pt")
    def form_view(self):
        buttons = []
        if "Reroll_Attributes" in self.request.POST:
            self._reroll()
        if (
            "Choose_Attributes" in self.request.POST
            and "choose" not in self.character.status
        ):
            self.character.status = {"attributes": "", "reroll": True, "choose": False}
        if "choose" not in self.character.status:
            buttons.append("Accept Attributes")
            if "reroll" not in self.character.status:
                buttons.append("Reroll Attributes")
            data = self.initialise_form()
            schema = self.schema(data)
        else:
            data = self.initialise_form()
            schema = self.choose_schema(data)
        buttons.append("Choose Attributes")
        form = deform.Form(
            schema,
            buttons=buttons,
        )
        if "Choose_Attributes" in self.request.POST:
            if self.character.status["choose"] is False:
                # choose attributes, but form not submitted yet
                self.character.status = {
                    "attributes": "",
                    "reroll": True,
                    "choose": True,
                }
                html = form.render()
            else:
                try:
                    captured = form.validate(self.request.POST.items())
                except deform.ValidationFailure as error:
                    html = error.render()
                else:
                    for attribute in captured["attributes"]:
                        value = int(captured["attributes"][attribute])
                        value += data["bonus_attributes"][attribute]
                        attribute_lower = (
                            f'{attribute.lower().replace(" ", "_")}_initial'
                        )
                        setattr(self.character, attribute_lower, value)
                    url = self.request.route_url("advances", uuid=self.character.uuid)
                    self.character.status = {"advances": ""}
                    return HTTPFound(location=url)
        elif "Accept_Attributes" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                matched = True
                for attribute in captured["attributes"]:
                    if (
                        int(captured["attributes"][attribute])
                        != self.character.status["attributes"][attribute]
                    ):
                        matched = False
                    value = int(captured["attributes"][attribute])
                    value += data["bonus_attributes"][attribute]
                    attribute_lower = f'{attribute.lower().replace(" ", "_")}_initial'
                    setattr(self.character, attribute_lower, value)
                if "reroll" not in self.character.status:
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
