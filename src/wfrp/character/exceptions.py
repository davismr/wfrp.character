from pyramid.httpexceptions import HTTPSeeOther
from pyramid.httpexceptions import HTTPUnauthorized
from pyramid.view import exception_view_config
from pyramid.view import forbidden_view_config
from pyramid.view import notfound_view_config


@notfound_view_config(renderer="wfrp.character:templates/exceptions/404.pt")
def notfound(request):
    request.response.status = 404
    return {}


@forbidden_view_config(renderer="wfrp.character:templates/exceptions/403.pt")
def forbidden(request):
    request.response.status = 403
    return {}


@exception_view_config(HTTPUnauthorized)
def unauthorized(request):
    location = request.route_url("homepage", _query={"came_from": request.path})
    message = "You need to login"
    request.session.flash(message, "error")
    return HTTPSeeOther(location)
