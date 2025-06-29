import bcrypt
from pyramid.security import Allowed
from pyramid_googleauth import GoogleSecurityPolicy


class SecurityPolicy(GoogleSecurityPolicy):

    def permits(self, request, _context, permission):
        return Allowed("allowed")


def hash_password(pw):
    pwhash = bcrypt.hashpw(pw.encode("utf8"), bcrypt.gensalt())
    return pwhash.decode("utf8")


def check_password(pw, hashed_pw):
    expected_hash = hashed_pw.encode("utf8")
    return bcrypt.checkpw(pw.encode("utf8"), expected_hash)
