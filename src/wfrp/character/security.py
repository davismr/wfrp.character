from pyramid.httpexceptions import HTTPNotFound
from pyramid.security import Allowed
from pyramid.security import Denied
from pyramid_googleauth import GoogleSecurityPolicy


class SecurityPolicy(GoogleSecurityPolicy):

    def permits(self, request, _context, permission):
        breakpoint()
        if not request.registry.settings.get("wfrp.character.enable_auth"):
            if permission == "account":
                raise HTTPNotFound
            return Allowed("allowed")
        return Denied("denied")
