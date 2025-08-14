import pytest

from wfrp.character.data.careers.careers import CAREER_DATA
from wfrp.character.data.talents import TALENT_DATA
from wfrp.character.data.talents import TALENT_LIST
from wfrp.character.data.talents import get_random_talent


@pytest.mark.data
def test_get_talent():
    talent = get_random_talent(66)
    assert talent == "Resistance (Any)"


@pytest.mark.data
def test_random_talents():
    for talent in TALENT_LIST.values():
        assert talent.split(" (")[0] in TALENT_DATA


@pytest.mark.data
def test_talent_descriptions():
    for talent in TALENT_DATA:
        assert TALENT_DATA[talent]["description"], talent


@pytest.mark.data
def test_talents():
    missing = []
    for career_data in CAREER_DATA:
        for career in CAREER_DATA[career_data]:
            for talent in CAREER_DATA[career_data][career]["talents"]:
                talent = talent.split(" (")[0]
                if talent not in TALENT_DATA:
                    missing.append(talent)
    assert not missing, sorted(missing)
