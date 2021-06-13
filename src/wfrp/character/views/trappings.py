import colander
import deform
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.career_data import CAREER_DATA
from wfrp.character.trappings import CLASS_TRAPPINGS
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
            title="Class Trappings",
            name="class_trappings",
        )
        for trapping in data["class_trappings"]:
            class_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    widget=deform.widget.TextInputWidget(template="readonly/textinput"),
                    missing="",
                    name=trapping,
                )
            )
        career_schema = colander.SchemaNode(
            colander.Mapping(),
            title="Career Trappings",
            name="career_trappings",
        )
        for trapping in data["class_trappings"]:
            career_schema.add(
                colander.SchemaNode(
                    colander.String(),
                    widget=deform.widget.TextInputWidget(template="readonly/textinput"),
                    missing="",
                    name=trapping,
                )
            )
        money_schema = colander.SchemaNode(
            colander.Mapping(),
            title="Money",
            name="money",
        )
        money_schema.add(
            colander.SchemaNode(
                colander.String(),
                widget=deform.widget.TextInputWidget(template="readonly/textinput"),
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
        form = deform.Form(schema, buttons=("Choose trappings",))
        if "Choose_trappings" in self.request.POST:
            try:
                form.validate(self.request.POST.items())
            except deform.ValidationFailure as error:
                html = error.render()
            else:
                data = self.character.status["trappings"]
                self.character.trappings = (
                    data["class_trappings"] + data["career_trappings"]
                )
                self.character.wealth = data["money"]
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
