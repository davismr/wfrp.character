from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.view import view_defaults

from wfrp.character.career_data import CAREER_DATA
from wfrp.character.views.attributes import ATTRIBUTES
from wfrp.character.views.base_view import BaseView


@view_defaults(route_name="advances")
class AdvancesViews(BaseView):
    @view_config(request_method="GET", renderer=__name__ + ":../templates/advances.pt")
    def get_view(self):
        attributes = {}
        for attribute in ATTRIBUTES:
            attribute_lower = attribute.lower().replace(" ", "_")
            attributes[attribute] = getattr(self.character, attribute_lower)
        career_data = CAREER_DATA[self.character.career]
        career_details = career_data[list(career_data)[1]]
        career_advances = career_details["attributes"]
        return {"attributes": attributes, "advances": career_advances}

    @view_config(request_method="POST", renderer=__name__ + ":../templates/advances.pt")
    def submit_view(self):
        for attribute in self.request.POST:
            if self.request.POST[attribute]:
                attribute_lower = attribute.lower().replace(" ", "_")
                current_value = getattr(self.character, attribute_lower)
                new_value = current_value + int(self.request.POST[attribute])
                setattr(self.character, attribute_lower, new_value)
        url = self.request.route_url("species_skills", uuid=self.character.uuid)
        self.character.status = {"species_skills": ""}
        return HTTPFound(location=url)
