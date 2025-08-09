from dataclasses import dataclass

import pytest
from pyramid import testing

from wfrp.character.application import dbsession
from wfrp.character.views.experience import ExperienceViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_form_view(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.career_title = "Recruit"
    new_character.status = {"complete": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    response = view.form_view()
    assert isinstance(response["form"], str)


@pytest.mark.views
def test_increase_characteristic(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.career_title = "Recruit"
    new_character.weapon_skill_initial = 40
    new_character.weapon_skill_advances = 9
    new_character.experience = 200
    new_character.status = {"complete": ""}
    payload = {
        "__formid__": "characteristic_form",
        "increase_characteristic": {"characteristic": "weapon_skill"},
        "Select_Name": "Select_Name",
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    view.form_view()
    assert new_character.weapon_skill == 50
    assert new_character.weapon_skill_advances == 10
    assert new_character.experience == 170
    assert new_character.experience_spent == 30
    # submit the form a second time with the same payload, which costs extra experience
    view.form_view()
    assert new_character.weapon_skill == 51
    assert new_character.weapon_skill_advances == 11
    assert new_character.experience == 130
    assert new_character.experience_spent == 70


@pytest.mark.views
def test_increase_characteristic_too_much(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.career_title = "Recruit"
    new_character.weapon_skill_initial = 40
    new_character.weapon_skill_advances = 9
    new_character.experience = 20
    new_character.status = {"complete": ""}
    payload = {
        "__formid__": "characteristic_form",
        "increase_characteristic": {"characteristic": "weapon_skill"},
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    response = view.form_view()
    assert (
        "You do not have enought experience to increase Weapon Skill, you need 30 XP"
    ) in response["form"]
    assert new_character.weapon_skill == 49
    assert new_character.weapon_skill_advances == 9
    assert new_character.experience == 20
    assert new_character.experience_spent == 0


@pytest.mark.views
def test_increase_unowned_skill(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.career_title = "Recruit"
    new_character.skills = {"Language (Battle)": 9, "Play (Drum)": 14}
    new_character.experience = 200
    new_character.status = {"complete": ""}
    payload = {
        "__formid__": "skill_form",
        "increase_skill": {"skill": "Athletics"},
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    view.form_view()
    assert new_character.skills["Athletics"] == 1
    assert new_character.experience == 190
    assert new_character.experience_spent == 10


@pytest.mark.views
def test_increase_existing_skill(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.career_title = "Recruit"
    new_character.skills = {"Athletics": 5, "Language (Battle)": 9, "Play (Drum)": 14}
    new_character.experience = 200
    new_character.status = {"complete": ""}
    payload = {
        "__formid__": "skill_form",
        "increase_skill": {"skill": "Language (Battle)"},
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    view.form_view()
    assert new_character.skills["Language (Battle)"] == 10
    assert new_character.experience == 185
    assert new_character.experience_spent == 15
    view.form_view()
    assert new_character.skills["Language (Battle)"] == 11
    assert new_character.experience == 165
    assert new_character.experience_spent == 35


@pytest.mark.views
def test_increase_choice_skill(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.career_title = "Recruit"
    new_character.skills = {"Language (Battle)": 9, "Play (Drum)": 14}
    new_character.experience = 200
    new_character.status = {"complete": ""}
    payload = {
        "__formid__": "skill_form",
        "increase_skill": {"skill": "Play (Drum)"},
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    view.form_view()
    assert new_character.skills["Play (Drum)"] == 15


@pytest.mark.views
def test_multiple_grouped_skills(new_character):
    new_character.species = "Human"
    new_character.career = "Pit Fighter"
    new_character.career_title = "Pugilist"
    new_character.skills = {
        "Melee (Basic)": 4,
        "Melee (Fencing)": 9,
        "Melee (Brawling)": 14,
    }
    new_character.experience = 200
    new_character.status = {"complete": ""}
    request = testing.DummyRequest()
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    response = view.form_view()
    assert response["form"].count("Melee (Basic) (4)") == 1
    assert response["form"].count("Melee (Fencing) (9)") == 1
    assert response["form"].count("Melee (Brawling) (14)") == 1
    payload = {
        "__formid__": "skill_form",
        "increase_skill": {"skill": "Melee (Basic)"},
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    view.form_view()
    assert new_character.skills["Melee (Basic)"] == 5


@pytest.mark.views
def test_increase_skill_too_much(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.career_title = "Recruit"
    new_character.skills = {"Athletics": 9, "Play (Drum)": 14}
    new_character.experience = 10
    new_character.status = {"complete": ""}
    payload = {
        "__formid__": "skill_form",
        "increase_skill": {"skill": "Athletics"},
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    response = view.form_view()
    assert (
        "You do not have enought experience to increase Athletics, you need 15 XP"
    ) in response["form"]
    assert new_character.skills["Athletics"] == 9
    assert new_character.experience == 10
    assert new_character.experience_spent == 0


@pytest.mark.views
def test_increase_talent(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.career_title = "Recruit"
    new_character.talents = {"Marksman": 1}
    new_character.experience = 200
    new_character.status = {"complete": ""}
    payload = {
        "__formid__": "talent_form",
        "add_talent": {"talent": "Marksman"},
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    view.form_view()
    assert new_character.talents["Marksman"] == 2
    assert new_character.experience == 0
    assert new_character.experience_spent == 200


@pytest.mark.views
def test_add_talent(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.career_title = "Recruit"
    new_character.talents = {"Marksman": 1}
    new_character.experience = 200
    new_character.status = {"complete": ""}
    payload = {
        "__formid__": "talent_form",
        "add_talent": {"talent": "Warrior Born"},
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    view.form_view()
    assert new_character.talents["Warrior Born"] == 1
    assert new_character.experience == 100
    assert new_character.experience_spent == 100


@pytest.mark.views
def test_talent_too_much(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.career_title = "Recruit"
    new_character.experience = 50
    new_character.status = {"complete": ""}
    payload = {
        "__formid__": "talent_form",
        "add_talent": {"talent": "Warrior Born"},
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    response = view.form_view()
    assert (
        "You do not have enought experience to increase Warrior Born, you need 100 XP"
    ) in response["form"]
    assert new_character.talents == {}
    assert new_character.experience == 50
    assert new_character.experience_spent == 0
