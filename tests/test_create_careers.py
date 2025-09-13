from dataclasses import dataclass

from pyramid import testing
from pyramid.httpexceptions import HTTPFound
import pytest

from wfrp.character.application import dbsession
from wfrp.character.views.create_character.career import CareerViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.create
def test_initialise_form(new_character):
    new_character.species = "Wood Elf"
    new_character.status = {"career": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerViews(request)
    response = view.initialise_form()
    assert isinstance(response, dict)
    assert "career_choice" in response
    assert len(response["career_choice"]) == 1
    assert "career_list" in response
    assert response["career_choice"][0] not in response["career_list"]


@pytest.mark.create
def test_initialise_form_seafarer(new_character):
    new_character.species = "High Elf"
    new_character.expansions = ["sea_of_claws"]
    new_character.status = {"career": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerViews(request)
    response = view.initialise_form()
    assert isinstance(response, dict)
    assert "career_choice" in response
    assert len(response["career_choice"]) == 1
    assert "career_list" in response
    assert response["career_choice"] not in response["career_list"]
    assert "Smuggler" not in response["career_list"]
    if response["career_choice"][0] != "Ship’s Gunner":
        assert "Ship’s Gunner" in response["career_list"]


@pytest.mark.create
def test_initialise_form_tilean(new_character):
    new_character.species = "Human (Tilean)"
    new_character.expansions = ["up_in_arms"]
    new_character.status = {"career": ["Flagellant"]}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerViews(request)
    response = view.initialise_form()
    assert isinstance(response, dict)
    assert "career_choice" in response
    assert response["career_choice"] == ["Flagellant", "Nun", "Priest"]
    assert response["career_choice"] == new_character.status["career"]


@pytest.mark.create
def test_initialise_form_tilean_multiple(new_character):
    new_character.species = "Human (Tilean)"
    new_character.expansions = ["up_in_arms"]
    new_character.status = {"career": ["Cavalryman", "Soldier", "Warrior Priest"]}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerViews(request)
    response = view.initialise_form()
    assert isinstance(response, dict)
    assert "career_choice" in response
    assert len(response["career_choice"]) == 6
    assert response["career_choice"] == [
        "Cavalryman",
        "Soldier",
        "Warrior Priest",
        "Light Cavalry",
        "Pikeman",
        "Priest of Myrmidia",
    ]
    assert response["career_choice"] == new_character.status["career"]


@pytest.mark.create
def test_form_view(new_character):
    new_character.species = "Wood Elf"
    new_character.status = {"career": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerViews(request)
    response = view.form_view()
    assert "form" in response
    assert "or reroll for 3 choices and" in response["form"]


@pytest.mark.create
def test_reroll_view(new_character):
    new_character.species = "Human"
    new_character.status = {"career": ["Soldier"]}
    request = testing.DummyRequest(
        post={
            "Reroll": "Reroll",
        }
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    choices = new_character.status["career"]
    assert len(choices) == 3
    assert "Soldier" in choices
    assert "or reroll for 3 choices and" not in response["form"]


@pytest.mark.create
def test_reroll_view_seafarer(new_character):
    new_character.expansions = ["sea_of_claws"]
    new_character.species = "Human"
    new_character.status = {"career": ["Beachcomber"]}
    request = testing.DummyRequest(
        post={
            "Reroll": "Reroll",
        }
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    choices = new_character.status["career"]
    assert len(choices) == 3
    assert "Beachcomber" in choices
    assert "or reroll for 3 choices and" not in response["form"]


@pytest.mark.create
def test_invalid_number_careers(new_character):
    new_character.species = "Human"
    new_character.status = {"career": ["Soldier", "Beggar"]}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerViews(request)
    with pytest.raises(NotImplementedError) as error:
        view.form_view()
    assert str(error.value) == "Incorrect number of career choices"


@pytest.mark.create
@pytest.mark.parametrize(
    "career_choice, experience",
    [(["Soldier"], 50), (["Soldier", "Seaman", "Bawd"], 25), (["Bawd"], 0)],
)
def test_submit_experience(new_character, career_choice, experience):
    new_character.species = "Human"
    new_character.status = {"career": career_choice}
    if career_choice == ["Bawd"]:
        request = testing.DummyRequest(
            post={
                "random_career": {"random_career": ""},
                "career": {"career": "Soldier"},
                "Choose_Career": "Choose_Career",
            }
        )
    else:
        request = testing.DummyRequest(
            post={
                "random_career": {"random_career": "Soldier"},
                "career": {"career": ""},
                "Choose_Career": "Choose_Career",
            }
        )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerViews(request)
    assert new_character.experience == 0
    response = view.form_view()
    assert isinstance(response, HTTPFound)
    assert new_character.experience == experience


@pytest.mark.create
def test_invalid_submit(new_character):
    new_character.species = "Human"
    new_character.status = {"career": ["Seaman"]}
    request = testing.DummyRequest(
        post={
            "random_career": {"random_career": "Seaman"},
            "career": {"career": "Soldier"},
            "Choose_Career": "Choose_Career",
        }
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "You can only select a single career" in response["form"]


@pytest.mark.create
def test_invalid_none(new_character):
    new_character.species = "Human"
    new_character.status = {"career": ["Seaman"]}
    request = testing.DummyRequest(
        post={
            "Choose_Career": "Choose_Career",
        }
    )
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="career")
    request.matchdict = {"id": str(new_character.id)}
    view = CareerViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "You have to select a career" in response["form"]
