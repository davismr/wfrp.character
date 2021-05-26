def includeme(config):
    config.add_route("homepage", "/")
    config.add_route("new_character", "/character/new")
    config.add_route("species", "/character/{uuid}/species")
    config.add_route("career", "/character/{uuid}/career")
    config.add_route("attributes", "/character/{uuid}/new")
    config.scan("wfrp.character.views")
