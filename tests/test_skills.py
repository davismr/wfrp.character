import pytest

from wfrp.character.data.careers import CAREER_DATA
from wfrp.character.data.skills import SKILL_DATA


@pytest.mark.data
def test_skill_characteristics():
    for skill in SKILL_DATA:
        assert SKILL_DATA[skill]["characteristic"]


@pytest.mark.data
def test_skill():
    missing = []
    for career_data in CAREER_DATA:
        for career in CAREER_DATA[career_data]:
            if career == "class":
                continue
            for skill in CAREER_DATA[career_data][career]["skills"]:
                skill = skill.split(" (")[0]
                if skill not in SKILL_DATA:
                    missing.append(skill)
    assert not missing, sorted(missing)
