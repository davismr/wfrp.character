from dataclasses import dataclass

import pytest
from pyramid import testing

from wfrp.character.views.experience import ExperienceViews


@dataclass
class DummyRoute:
    name: str


@pytest.mark.views
def test_form_view(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.status = {"complete": ""}
    request = testing.DummyRequest()
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"uuid": new_character.uuid}
    view = ExperienceViews(request)
    response = view.form_view()
    assert isinstance(response["form"], str)


@pytest.mark.views
def test_increase_characteristic(new_character):
    new_character.species = "Wood Elf"
    new_character.career = "Soldier"
    new_character.weapon_skill_initial = 40
    new_character.weapon_skill_advances = 9
    new_character.experience = 200
    new_character.status = {"complete": ""}
    payload = {
        "__formid__": "characteristic_form",
        "increase_characteristics": {"characteristics": "weapon_skill"},
        "Select_Name": "Select_Name",
    }
    request = testing.DummyRequest(post=payload)
    request.matched_route = DummyRoute(name="experience")
    request.matchdict = {"uuid": new_character.uuid}
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
