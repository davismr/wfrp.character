from wfrp.character.database import db
from wfrp.character.models.character import Character


def test_get_view(client):
    character = Character()
    db.session.add(character)
    db.session.commit()
    response = client.get(f"/build/species/{str(character.id)}")
    assert response.status_code == 200
    assert "<h1>Species</h1>" in response.text


def test_post_view(client):
    character = Character()
    db.session.add(character)
    db.session.commit()
    response = client.post(
        f"/build/species/{str(character.id)}",
        data={
            "species": "Dwarf",
        },
    )
    assert response.status_code == 302
    assert response.location == f"/build/career/{str(character.id)}"
    assert character.species == "Dwarf"
    assert character.fate == 2
    assert character.fortune in [2, 3]
    assert character.movement == 3
    assert character.status == "career"
