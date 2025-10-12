import pytest

from wfrp.character.data.magic.miracles import get_miracles


@pytest.mark.data
def test_manann():
    miracles = get_miracles("Manann")
    assert len(miracles) == 6
    miracles = get_miracles("Manann", ["sea_of_claws"])
    assert len(miracles) == 14
    assert list(miracles.keys())[-1] == "Waterwalk"
