import pytest

from wfrp.character.career_data import get_career
from wfrp.character.utils import roll_2d10
from wfrp.character.utils import roll_d10
from wfrp.character.utils import roll_d100


@pytest.mark.package
def test_roll_d10():
    for i in range(1000):
        result = roll_d10()
        assert result >= 1
        assert result <= 10


@pytest.mark.package
def test_roll_2d10():
    for i in range(1000):
        result = roll_2d10()
        assert result >= 2
        assert result <= 20


@pytest.mark.package
def test_roll_d100():
    for i in range(1000):
        result = roll_d100()
        assert result >= 1
        assert result <= 100


@pytest.mark.package
def test_get_career():
    assert get_career("Wood Elf", 1) == "Scholar"
    assert get_career("Wood Elf", 70) == "Bounty Hunter"
    assert get_career("Wood Elf", 2) == "Wizard"
    assert get_career("Wood Elf", 100) == "Soldier"
