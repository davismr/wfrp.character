import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.armour import ARMOUR_DATA
from wfrp.character.data.class_trappings import get_class_trappings
from wfrp.character.data.weapons import WEAPONS_DATA
from wfrp.character.utils import roll_d10
from wfrp.character.views.create_character.base_create import BaseCreateView


@view_defaults(
    renderer="wfrp.character:templates/forms/base_form.pt",
    permission="create_character",
)
class TrappingsViews(BaseCreateView):
    def _get_wealth(self, tier, standing):
        if tier == "Brass":
            wealth = {"brass": 0}
            for i in range(standing):
                wealth["brass"] += roll_d10() + roll_d10()
        elif tier == "Silver":
            wealth = {"silver": 0}
            for i in range(standing):
                wealth["silver"] += roll_d10()
        elif tier == "Gold":
            wealth = {"gold": standing}
        else:
            raise NotImplementedError(f"{tier} is not defined")
        return wealth

    def initialise_form(self):
        if self.character.create_data["trappings"]:
            return self.character.create_data["trappings"]
        career_data = self.character.career_data()
        class_trappings = get_class_trappings(self.character.career_class)
        career_details = career_data[self.character.career_title]
        career_trappings = career_details["trappings"]
        wealth = self._get_wealth(
            career_details["status"]["tier"], career_details["status"]["standing"]
        )
        data = {
            "class_trappings": class_trappings,
            "career_trappings": career_trappings,
            "wealth": wealth,
        }
        self.character.create_data = {"trappings": data}
        return data

    def schema(self, data):
        schema = colander.SchemaNode(
            colander.Mapping(), title="Class and Career Trappings"
        )
        class_schema = colander.SchemaNode(
            colander.Mapping(),
            name="class_trappings",
        )
        for trapping in data["class_trappings"]:
            choices = []
            for item in trapping.split(" or "):
                choices.append((item, item))
            class_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    name=trapping,
                    validator=colander.OneOf([x[0] for x in choices]),
                    widget=deform.widget.RadioChoiceWidget(
                        values=choices,
                        inline=True,
                        readonly=len(choices) == 1,
                    ),
                    missing=choices[0][0],
                )
            )
        career_schema = colander.SchemaNode(
            colander.Mapping(),
            name="career_trappings",
        )
        for trapping in data["career_trappings"]:
            choices = []
            for item in trapping.split(" or "):
                choices.append((item, item))
            career_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    name=trapping,
                    validator=colander.OneOf([x[0] for x in choices]),
                    widget=deform.widget.RadioChoiceWidget(
                        values=choices,
                        inline=True,
                        readonly=len(choices) == 1,
                    ),
                    missing=choices[0][0],
                )
            )
        wealth_schema = colander.SchemaNode(
            colander.Mapping(),
            name="wealth",
        )
        if "brass" in data["wealth"]:
            default_wealth = f"{data['wealth']['brass']} Brass Pennies"
        elif "silver" in data["wealth"]:
            default_wealth = f"{data['wealth']['silver']} Silver Shillings"
        elif "gold" in data["wealth"]:
            default_wealth = f"{data['wealth']['gold']} Gold Crowns"
        wealth_schema.add(
            colander.SchemaNode(
                colander.String(),
                widget=deform.widget.TextInputWidget(readonly=True),
                default=default_wealth,
                missing="",
                name="wealth_field",
            )
        )
        schema.add(class_schema)
        schema.add(career_schema)
        schema.add(wealth_schema)
        return schema

    @view_config(route_name="trappings")
    def form_view(self):
        data = self.initialise_form()
        schema = self.schema(data)
        form = deform.Form(schema, buttons=("Choose trappings",))
        if "Choose_trappings" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                self.update_values(captured)
                url = self.request.route_url("details", id=self.character.id)
                self.character.create_data = {"details": ""}
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

    def update_values(self, captured):  # noqa: C901
        all_items = []
        items = (
            self.character.create_data["trappings"]["class_trappings"]
            + self.character.create_data["trappings"]["career_trappings"]
        )
        for item in items:
            if " or " in item:
                if item in captured["class_trappings"]:
                    all_items.append(captured["class_trappings"][item])
                else:
                    all_items.append(captured["career_trappings"][item])
            else:
                all_items.append(item)
        for item in set(all_items):
            if item in WEAPONS_DATA:
                self.character.weapons.append(item)
            elif item.split()[0] in WEAPONS_DATA:
                self.character.weapons.append(item.split()[0])
            elif item in ARMOUR_DATA:
                self.character.armour.append(item)
            self.character.trappings.append(item)
        self.character.weapons.sort()
        self.character.armour.sort()
        self.character.trappings.sort()
        wealth = self.character.create_data["trappings"]["wealth"]
        if "brass" in wealth:
            self.character.brass_pennies = wealth["brass"]
        elif "silver" in wealth:
            self.character.silver_shillings = wealth["silver"]
        if "gold" in wealth:
            self.character.gold_crowns = wealth["gold"]
