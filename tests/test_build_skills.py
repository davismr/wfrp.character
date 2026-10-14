from wfrp.character.database import db
from wfrp.character.models.character import Character


def test_get_view(client):
    character = Character(species="Human", career="Knave", career_title="Hustler")
    db.session.add(character)
    db.session.commit()
    response = client.get(f"/build/skills/{str(character.id)}")
    assert response.status_code == 200
    assert "<h1>Species and Career Skills</h1>" in response.text
    assert "Language (Wastelander)" in response.text
    assert "Stealth (Urban)" in response.text


def test_post_view(client):
    character = Character(species="Human", career="Knave", career_title="Hustler")
    db.session.add(character)
    db.session.commit()
    response = client.post(
        f"/build/skills/{str(character.id)}",
        data={
            "species_skills": ["Language (Wastelander)", "Charm"],
            "Bribery": "1",
            "Charm": "2",
        },
    )
    assert response.status_code == 302
    assert response.location == f"/build/skills/{str(character.id)}"
    assert character.skills == {"Bribery": 5, "Charm": 15, "Language (Wastelander)": 5}
