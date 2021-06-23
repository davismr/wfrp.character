def includeme(config):
    config.add_route("homepage", "/")
    config.add_route("links", "/links")
    config.add_route("new_character", "/character/new")
    config.add_route("species", "/character/{uuid}/species")
    config.add_route("career", "/character/{uuid}/career")
    config.add_route("attributes", "/character/{uuid}/attributes")
    config.add_route("advances", "/character/{uuid}/advances")
    config.add_route("career_skills", "/character/{uuid}/career_skills")
    config.add_route("species_skills", "/character/{uuid}/species_skills")
    config.add_route("trappings", "/character/{uuid}/trappings")
    config.add_route("details", "/character/{uuid}/details")
    config.add_route("name", "/character/{uuid}/name")
    config.add_route("character", "/character/{uuid}/view")
    config.scan("wfrp.character.views")
