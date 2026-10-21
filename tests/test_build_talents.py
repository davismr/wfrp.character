from wfrp.character.database import db
from wfrp.character.models.character import Character


def test_get_view(client):
    character = Character(
        species="Dwarf", career="Hunter", career_title="Trapper", status="Talents"
    )
    db.session.add(character)
    db.session.commit()
    response = client.get(f"/create/talents/{str(character.id)}")
    assert response.status_code == 200
    assert "<h1>Species and Career Talents</h1>" in response.text
    assert "Magic Resistance" in response.text
    assert "Striding Gait (All)" in response.text


def test_post_view(client):
    character = Character(
        species="Dwarf", career="Hunter", career_title="Trapper", status="Talents"
    )
    db.session.add(character)
    db.session.commit()
    response = client.post(
        f"/create/talents/{str(character.id)}",
        data={
            "career_talents": "Striding Gait (All)",
            "Magic Resistance": "Magic Resistance",
            "Night Vision": "Night Vision",
        },
    )
    assert response.status_code == 302
    assert response.location == f"/create/magic/{str(character.id)}"
    assert "Striding Gait (All)" in character.talents
    assert "Magic Resistance" in character.talents
    assert character.talents["Striding Gait (All)"] == 1
