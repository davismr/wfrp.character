import uuid

import factory
from faker import Factory as FakerFactory

from wfrp.character.data.careers import list_careers
from wfrp.character.data.species import SPECIES_DATA
from wfrp.character.data.species import SPECIES_LIST
from wfrp.character.models import Character

faker = FakerFactory.create()


class CharacterFactory(factory.Factory):
    uuid = factory.LazyAttribute(lambda x: str(uuid.uuid4()))
    name = factory.LazyAttribute(lambda x: faker.name())
    species = factory.LazyAttribute(lambda x: x.species_param)
    career = factory.LazyAttribute(
        lambda x: faker.random_element(list_careers(x.species_param))
    )
    height = 72
    hair = factory.LazyAttribute(
        lambda x: faker.random_element(
            SPECIES_DATA[x.species_param]["hair_colour"].values()
        )
    )
    eyes = factory.LazyAttribute(
        lambda x: faker.random_element(
            SPECIES_DATA[x.species_param]["eye_colour"].values()
        )
    )
    status = {"complete": ""}
    trappings = ["Fine Clothing", "Cloak", "Tinderbox"]

    class Params:
        species_param = factory.LazyAttribute(
            lambda x: faker.random_element(SPECIES_LIST)
        )

    class Meta:
        model = Character
