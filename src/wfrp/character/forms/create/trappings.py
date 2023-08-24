import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.data.armour import ARMOUR_DATA
from wfrp.character.data.careers import CAREER_DATA
from wfrp.character.data.class_trappings import CLASS_TRAPPINGS
from wfrp.character.data.weapons import WEAPONS_DATA
from wfrp.character.utils import roll_d10
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="trappings")
class TrappingsViews(BaseView):
    def _get_money(self, tier, standing):
        if tier == "Brass":
            money = {"brass pennies": 0}
            for i in range(standing):
                money["brass pennies"] += roll_d10() + roll_d10()
        elif tier == "Silver":
            money = {"silver shillings": 0}
            for i in range(standing):
                money["silver shillings"] += roll_d10()
        elif tier == "Gold":
            money = {"Gold crown": standing}
        else:
            raise NotImplementedError(f"{tier} is not defined")
        return money

    def initialise_form(self):
        if self.character.status["trappings"]:
            return self.character.status["trappings"]
        career_data = CAREER_DATA[self.character.career]
        class_trappings = CLASS_TRAPPINGS[career_data["class"]]
        # TODO find a better way to do this
        career_details = career_data[list(career_data)[1]]
        career_trappings = career_details["trappings"]
        money = self._get_money(
            career_details["status"]["tier"], career_details["status"]["standing"]
        )
        data = {
            "class_trappings": class_trappings,
            "career_trappings": career_trappings,
            "money": money,
        }
        self.character.status = {"trappings": data}
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
                    widget=deform.widget.RadioChoiceWidget(values=choices, inline=True),
                    default=trapping,
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
                    widget=deform.widget.RadioChoiceWidget(values=choices, inline=True),
                    default=trapping,
                )
            )
        money_schema = colander.SchemaNode(
            colander.Mapping(),
            name="money",
        )
        money_schema.add(
            colander.SchemaNode(
                colander.String(),
                widget=deform.widget.TextInputWidget(readonly=True),
                missing="",
                name="money_field",
            )
        )
        schema.add(class_schema)
        schema.add(career_schema)
        schema.add(money_schema)
        return schema

    @view_config(renderer="wfrp.character:templates/trappings.pt")
    def form_view(self):
        data = self.initialise_form()
        schema = self.schema(data)
        values = {
            "money": {
                "money_field": (
                    f"{data['money'][list(data['money'])[0]]} {list(data['money'])[0]}"
                )
            }
        }
        form = deform.Form(schema, buttons=("Choose trappings",), appstruct=values)
        if "Choose_trappings" in self.request.POST:
            try:
                captured = form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                all_items = []
                items = (
                    self.character.status["trappings"]["class_trappings"]
                    + self.character.status["trappings"]["career_trappings"]
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
                    elif item in ARMOUR_DATA:
                        self.character.armour.append(item)
                    else:
                        self.character.trappings.append(item)
                self.character.weapons.sort()
                self.character.armour.sort()
                self.character.trappings.sort()
                self.character.wealth = self.character.status["trappings"]["money"]
                url = self.request.route_url("details", uuid=self.character.uuid)
                self.character.status = {"details": ""}
                return HTTPFound(location=url)
        else:
            html = form.render()

        static_assets = form.get_widget_resources()
        return {
            "form": html,
            "css_links": static_assets["css"],
            "js_links": static_assets["js"],
        }
