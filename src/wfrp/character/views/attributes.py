from pyramid.view import view_config

from wfrp.character.utils import roll_2d10


@view_config(
    route_name="attributes",
    request_method="GET",
    renderer=__name__ + ":../templates/attributes.pt",
)
def attributes_view(request):
    return {
        "rolls": [
            roll_2d10(),
            roll_2d10(),
            roll_2d10(),
            roll_2d10(),
            roll_2d10(),
            roll_2d10(),
        ]
    }
