import pytest

from wfrp.character.data.class_trappings import get_class_trappings


@pytest.mark.data
def test_class_trappings_academics():
    trappings = get_class_trappings("Academics")
    assert "Writing Kit" in trappings


@pytest.mark.data
def test_class_trappings_burghers():
    trappings = get_class_trappings("Burghers")
    assert "Lunch" in trappings


@pytest.mark.data
def test_class_trappings_courtiers():
    trappings = get_class_trappings("Courtiers")
    assert "Tweezers" in trappings


@pytest.mark.data
def test_class_trappings_peasants():
    trappings = get_class_trappings("Peasants")
    assert "Rations, 1 day" in trappings
    assert "Sling Bag" in trappings


@pytest.mark.data
def test_class_trappings_rangers():
    trappings = get_class_trappings("Rangers")
    assert "Tinderbox" in trappings


@pytest.mark.data
def test_class_trappings_riverfolk():
    trappings = get_class_trappings("Riverfolk")
    assert "Flask of Spirits" in trappings


@pytest.mark.data
def test_class_trappings_rogues():
    trappings = get_class_trappings("Rogues")
    assert "2 Candles" in trappings


@pytest.mark.data
def test_class_trappings_warriors():
    trappings = get_class_trappings("Warriors")
    assert "Hand Weapon" in trappings


@pytest.mark.data
def test_class_trappings_invalid():
    with pytest.raises(NotImplementedError):
        get_class_trappings("Not a species")
