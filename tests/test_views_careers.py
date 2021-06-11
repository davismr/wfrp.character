from dataclasses import dataclass

import pytest
from pyramid import testing
from pyramid.httpexceptions import HTTPFound

from wfrp.character.views.career import CareerViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_get_view(new_character):
    new_character.species = "Wood Elf"
    new_character.status = {"career": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"uuid": new_character.uuid}
    view = CareerViews(request)
    response = view.initialise_form()
    assert "career_choice" in response
    assert len(response["career_choice"]) == 1
    assert "career_list" in response
    assert response["career_choice"] not in response["career_list"]


@pytest.mark.views
def test_reroll_view(new_character):
    new_character.species = "Human"
    new_character.status = {"career": "Soldier"}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"uuid": new_character.uuid}
    view = CareerViews(request)
    response = view.reroll_career_view()
    assert response is None
    choices = new_character.status["career"].split(",")
    assert len(choices) == 3
    assert "Soldier" in choices


@pytest.mark.current
@pytest.mark.parametrize(
    "career_choice, experience",
    [("Soldier", 50), ("Soldier,Seaman,Bawd", 25), ("Bawd", 0)],
)
def test_submit_experience(new_character, career_choice, experience):
    new_character.species = "Human"
    new_character.status = {"career": career_choice}
    if career_choice == "Bawd":
        request = testing.DummyRequest(
            post={
                "random_career": {"": ""},
                "career": {"": "Soldier"},
                "Choose_Career": "Choose_Career",
            }
        )
    else:
        request = testing.DummyRequest(
            post={
                "random_career": {"": "Soldier"},
                "career": {"": ""},
                "Choose_Career": "Choose_Career",
            }
        )
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"uuid": new_character.uuid}
    view = CareerViews(request)
    assert new_character.experience == 0
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.experience == experience
