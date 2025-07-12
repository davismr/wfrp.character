from pyramid.security import Allowed
from pyramid_googleauth import GoogleSecurityPolicy


class SecurityPolicy(GoogleSecurityPolicy):

    def permits(self, request, _context, permission):
        return Allowed("allowed")
