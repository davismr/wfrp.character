import pytest

from wfrp.character.data.magic.miracles import get_miracles


@pytest.mark.data
def test_manann():
    miracles = get_miracles("Manann")
    assert len(miracles) == 6
    miracles = get_miracles("Manann", ["sea_of_claws"])
    assert len(miracles) == 14
    assert list(miracles.keys())[-1] == "Waterwalk"


@pytest.mark.data
def test_taal():
    miracles = get_miracles("Taal")
    assert len(miracles) == 6
    miracles = get_miracles("Taal", ["deft_steps"])
    assert len(miracles) == 14
    assert list(miracles.keys())[-1] == "Wilderness Way"


@pytest.mark.data
def test_ranald_night_prowler():
    miracles = get_miracles("Ranald-Night-Prowler")
    assert len(miracles) == 12
    assert list(miracles.keys())[-2] == "The Heat Is Off"
    assert list(miracles.keys())[-1] == "You Ain’t Seen Me, Right?"


@pytest.mark.data
def test_ranald_deceiver():
    miracles = get_miracles("Ranald-Deceiver")
    assert len(miracles) == 10
    assert list(miracles.keys())[0] == "A Suitable Sucker"
    assert list(miracles.keys())[-1] == "You Ain’t Seen Me, Right?"


@pytest.mark.data
def test_ranald_gamester():
    miracles = get_miracles("Ranald-Gamester")
    assert len(miracles) == 10
    assert list(miracles.keys())[0] == "Bountiful Fortune"
    assert list(miracles.keys())[1] == "Cat’s Eyes"


@pytest.mark.data
def test_ranald_protector():
    miracles = get_miracles("Ranald-Protector")
    assert len(miracles) == 11
    assert list(miracles.keys())[0] == "An Invitation"
    assert list(miracles.keys())[-1] == "You Ain’t Seen Me, Right?"
