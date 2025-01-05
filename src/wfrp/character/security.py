import bcrypt
from pyramid.authentication import AuthTktCookieHelper
from pyramid.security import Allowed
from pyramid.security import Denied

from wfrp.character.models.user import User


def hash_password(pw):
    pwhash = bcrypt.hashpw(pw.encode("utf8"), bcrypt.gensalt())
    return pwhash.decode("utf8")


def check_password(pw, hashed_pw):
    expected_hash = hashed_pw.encode("utf8")
    return bcrypt.checkpw(pw.encode("utf8"), expected_hash)


USERS = {"editor": hash_password("editor"), "viewer": hash_password("viewer")}


class SecurityPolicy:
    def __init__(self, secret):
        self.authtkt = AuthTktCookieHelper(secret=secret)

    def identity(self, request):
        identity = self.authtkt.identify(request)
        if identity is not None:
            # XXX needs to be wrapped in try/except
            request.dbsession.query(User).filter(User.email == identity["userid"]).one()
            return identity

    def authenticated_userid(self, request):
        identity = self.identity(request)
        if identity is not None:
            return identity["userid"]

    def remember(self, request, userid, **kw):
        return self.authtkt.remember(request, userid, **kw)

    def forget(self, request, **kw):
        return self.authtkt.forget(request, **kw)

    def permits(self, request, context, permission):
        identity = self.identity(request)
        if identity is None:
            return Denied("User is not signed in.")
        if identity and permission == "create_character":
            return Allowed(
                f"Access granted for user {identity} for {permission} permission."
            )
        return Denied(f"Access denied for user {identity} for {permission} permission.")
