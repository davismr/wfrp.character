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

    @view_config(request_method="GET", renderer=__name__ + ":../templates/trappings.pt")
    def get_view(self):
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

    @view_config(
        request_method="POST", renderer=__name__ + ":../templates/trappings.pt"
    )
    def submit_view(self):
        data = self.character.status["trappings"]
        self.character.trappings = data["class_trappings"] + data["career_trappings"]
        self.character.wealth = data["money"]
        url = self.request.route_url("details", uuid=self.character.uuid)
        self.character.status = {"details": ""}
        return HTTPFound(location=url)
