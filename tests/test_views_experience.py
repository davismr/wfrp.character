from dataclasses import dataclass

from pyramid import testing
import pytest

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
    assert new_character.experience == 140
    assert new_character.experience_spent == 60
    view.form_view()
    assert new_character.weapon_skill == 52
    assert new_character.weapon_skill_advances == 12
    assert new_character.experience == 100
    assert new_character.experience_spent == 100
    # experience cost should be added for all three
    assert len(new_character.experience_cost) == 3
    assert new_character.experience_cost[0].cost == 30
    assert new_character.experience_cost[0].type == "characteristic"
    assert new_character.experience_cost[0].name == "weapon_skill"
    assert new_character.experience_cost[1].cost == 30
    assert new_character.experience_cost[2].cost == 40


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
        "You do not have enough experience to increase Weapon Skill, you need 30 XP"
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
    # experience cost should be added
    assert len(new_character.experience_cost) == 1
    assert new_character.experience_cost[0].cost == 10
    assert new_character.experience_cost[0].type == "skill"
    assert new_character.experience_cost[0].name == "Athletics"


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
    assert new_character.experience == 170
    assert new_character.experience_spent == 30
    view.form_view()
    assert new_character.skills["Language (Battle)"] == 12
    assert new_character.experience == 150
    assert new_character.experience_spent == 50


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
        "You do not have enough experience to increase Athletics, you need 15 XP"
    ) in response["form"]
    assert new_character.skills["Athletics"] == 9
    assert new_character.experience == 10
    assert new_character.experience_spent == 0


@pytest.mark.views
def test_increase_talent(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.career_title = "Recruit"
    new_character.intelligence_initial = 20
    new_character.talents = {"Diceman": 1}
    new_character.experience = 200
    new_character.status = {"complete": ""}
    payload = {
        "__formid__": "talent_form",
        "add_talent": {"talent": "Diceman"},
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    view.form_view()
    assert new_character.talents["Diceman"] == 2
    assert new_character.experience == 0
    assert new_character.experience_spent == 200
    # experience cost should be added
    assert len(new_character.experience_cost) == 1
    assert new_character.experience_cost[0].cost == 200
    assert new_character.experience_cost[0].type == "talent"
    assert new_character.experience_cost[0].name == "Diceman"


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
        "You do not have enough experience to increase Warrior Born, you need 100 XP"
    ) in response["form"]
    assert new_character.talents == {}
    assert new_character.experience == 50
    assert new_character.experience_spent == 0


@pytest.mark.current
def test_petty_magic(new_character):
    new_character.species = "Human"
    new_character.career = "Wizard"
    new_character.career_title = "Wizard’s Apprentice"
    new_character.willpower_initial = 14
    new_character.talents = {"Petty Magic": 1}
    new_character.spells = {"petty": ["Animal Friend", "Sleep"]}
    new_character.experience = 100
    new_character.status = {"complete": ""}
    payload = {
        "__formid__": "magic_form",
        "spells": {"petty_magic": "Purify Water"},
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert new_character.experience == 0
    assert new_character.spells == {"petty": ["Animal Friend", "Sleep", "Purify Water"]}


@pytest.mark.views
def test_miracle(new_character):
    new_character.species = "Human"
    new_character.career = "Nun"
    new_character.career_title = "Nun"
    new_character.talents = {"Invoke (Manann)": 1}
    new_character.spells = {"miracles": ["Waterwalk"]}
    new_character.experience = 100
    new_character.status = {"complete": ""}
    payload = {
        "__formid__": "miracles_form",
        "miracles": {"miracle": "Becalm"},
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert new_character.experience == 0
    assert new_character.spells == {"miracles": ["Waterwalk", "Becalm"]}


@pytest.mark.views
def test_advance_career(new_character):
    new_character.species = "Wood Elf"
    new_character.expansions = ["sea_of_claws"]
    new_character.career_class = "Seafarer"
    new_character.career = "Beachcomber"
    new_character.career_title = "Scavenger"
    new_character.career_path = ["Scavenger"]
    new_character.experience = 200
    new_character.status = {"complete": ""}
    payload = {
        "__formid__": "career_form",
        "change_career": {"advance_career": "Beachcomber"},
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    response = view.form_view()
    assert response.status_code == 302
    assert new_character.career_title == "Beachcomber"
    assert new_character.career_path == ["Scavenger", "Beachcomber"]
    assert new_character.experience == 0
    assert new_character.experience_spent == 200
    # experience cost should be added
    assert len(new_character.experience_cost) == 1
    assert new_character.experience_cost[0].cost == 200
    assert new_character.experience_cost[0].type == "career"
    assert new_character.experience_cost[0].name == "Beachcomber"


@pytest.mark.views
def test_advance_career_no_experience(new_character):
    new_character.species = "Wood Elf"
    new_character.expansions = ["sea_of_claws"]
    new_character.career_class = "Seafarer"
    new_character.career = "Beachcomber"
    new_character.career_title = "Scavenger"
    new_character.experience = 100
    new_character.status = {"complete": ""}
    payload = {
        "__formid__": "career_form",
        "change_career": {"advance_career": "Beachcomber"},
    }
    request = testing.DummyRequest(post=payload)
    request.dbsession = dbsession(request)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"id": str(new_character.id)}
    view = ExperienceViews(request)
    response = view.form_view()
    assert isinstance(response, dict)
    assert "You do not have enough experience to change career" in response["form"]
