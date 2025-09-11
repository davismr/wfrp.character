from dataclasses import dataclass

from pyramid import testing
from pyramid.httpexceptions import HTTPFound
import pytest

from wfrp.character.application import dbsession
from wfrp.character.data.careers.up_in_arms import UP_IN_ARMS_CAREERS
from wfrp.character.views.create_character.sub_career import SubCareerViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.create
def test_initialise_form(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.status = {"sub-career": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="sub-career")
    request.matchdict = {"id": str(new_character.id)}
    view = SubCareerViews(request)
    response = view.initialise_form()
    assert isinstance(response, dict)
    assert "sub_career" in response
    assert response["sub_career"] in UP_IN_ARMS_CAREERS["Soldier"].values()
    assert response["experience_loss"] == 0


@pytest.mark.create
def test_form_view(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.status = {"sub-career": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="sub-career")
    request.matchdict = {"id": str(new_character.id)}
    view = SubCareerViews(request)
    response = view.form_view()
    assert "form" in response
    assert "Siege Specialist" in response["form"]


@pytest.mark.create
@pytest.mark.parametrize(
    "experience, expected", [(0, 0), (20, 20), (25, 0), (50, 0), (45, 20), (70, 20)]
)
def test_submit_experience(new_character, experience, expected):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.experience = experience
    new_character.status = {"sub-career": "Archer"}
    request = testing.DummyRequest(
        post={
            "specialist_career": {"specialist_career": "Handgunner"},
            "Choose_Career": "Choose_Career",
        }
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="sub-career")
    request.matchdict = {"id": str(new_character.id)}
    view = SubCareerViews(request)
    assert new_character.experience == experience
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.experience == expected
    assert new_character.career == "Handgunner"
    assert new_character.career_title == "Handgunner Recruit"
    assert new_character.career_path == ["Handgunner Recruit"]
    assert new_character.career_tier == "Silver"
    assert new_character.career_standing == 1
