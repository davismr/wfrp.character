from wfrp.character.database import db
from wfrp.character.models.character import Character


def test_get_view(client):
    character = Character()
    db.session.add(character)
    db.session.commit()
    response = client.get("/")
    assert response.status_code == 200
    assert "<h1>Home</h1>" in response.text
    assert str(character.id) in response.text
