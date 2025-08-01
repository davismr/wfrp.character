from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPSeeOther
from pyramid.httpexceptions import HTTPUnauthorized
from pyramid.response import Response
from pyramid.view import exception_view_config
from pyramid.view import view_config


# @view_config(context=HTTPUnauthorized)
@exception_view_config(HTTPUnauthorized)
def failed_validation(exc, request):
    # If the view has two formal arguments, the first is the context.
    # The context is always available as ``request.context`` too.
    # breakpoint()
    return request.context
    location = request.route_url("homepage", _query={"came_from": request.path})
    # return HTTPSeeOther(location)
    breakpoint()

    msg = exc.args[0] if exc.args else ""
    response = Response("Failed validation: %s" % msg)
    response.status_int = 401
    return response
    # return HTTPFound(location='/', status=401)
