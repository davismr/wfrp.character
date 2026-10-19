from wfrp.character.database import db
from wfrp.character.models.character import Character


def test_get_view(client):
    character = Character(
        species="Human", career="Knave", career_title="Hustler", status="Skills"
    )
    db.session.add(character)
    db.session.commit()
    response = client.get(f"/build/skills/{str(character.id)}")
    assert response.status_code == 200
    assert "<h1>Species and Career Skills</h1>" in response.text
    assert "Language (Wastelander)" in response.text
    assert "Stealth (Urban)" in response.text


def test_post_view(client):
    character = Character(
        species="Human", career="Knave", career_title="Hustler", status="Skills"
    )
    db.session.add(character)
    db.session.commit()
    response = client.post(
        f"/build/skills/{str(character.id)}",
        data={
            "species_skills": ["Language (Wastelander)", "Charm", "Not", "A", "Skill"],
            "Bribery": "1",
            "Charm": "2",
            "Consume Alcohol": "3",
            "Stealth (Urban)": "2",
        },
    )
    assert response.status_code == 302
    assert response.location == f"/build/talents/{str(character.id)}"
    assert character.skills["Bribery"] == 5
    assert character.skills["Charm"] == 15
    assert character.skills["Consume Alcohol"] == 15
    assert character.skills["Language (Wastelander)"] == 5
    assert character.skills["Stealth (Urban)"] == 10


def test_species_skills_error(client):
    character = Character(
        species="Human", career="Knave", career_title="Hustler", status="Skills"
    )
    db.session.add(character)
    db.session.commit()
    response = client.post(
        f"/build/skills/{str(character.id)}",
        data={
            "species_skills": ["Language (Wastelander)", "Charm"],
            "Bribery": "1",
            "Charm": "2",
            "Consume Alcohol": "3",
            "Stealth (Urban)": "2",
        },
    )
    assert response.status_code == 200
    assert "The form has errors." in response.text


def test_career_skills_error(client):
    character = Character(
        species="Human", career="Knave", career_title="Hustler", status="Skills"
    )
    db.session.add(character)
    db.session.commit()
    response = client.post(
        f"/build/skills/{str(character.id)}",
        data={
            "species_skills": ["Language (Wastelander)", "Charm", "Not", "A", "Skill"],
            "Bribery": "1",
            "Charm": "2",
            "Consume Alcohol": "3",
            "Stealth (Urban)": "3",
        },
    )
    assert response.status_code == 200
    assert "The form has errors." in response.text
