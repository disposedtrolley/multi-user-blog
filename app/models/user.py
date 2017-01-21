from google.appengine.ext import db
from string import letters

import hashlib
import random


class User(db.Model):
    """Database model for users.
    """
    name = db.StringProperty(required=True)
    pw_hash = db.StringProperty(required=True)
    email = db.StringProperty()

    @classmethod
    def by_id(cls, uid):
        """Retrieves a single user by their id.
        """
        return cls.get_by_id(int(uid))

    @classmethod
    def by_name(cls, name):
        """Retrieves a single post by their username.
        """
        u = cls.all().filter("name =", name).get()
        return u

    @classmethod
    def register(cls, name, pw, email=None):
        """Creates a new User record.
        """
        pw_hash = cls.make_pw_hash(name, pw)
        return cls(name=name,
                    pw_hash=pw_hash,
                    email=email)

    @classmethod
    def login(cls, name, pw):
        """Validates the credentials of a login request.
        """
        u = cls.by_name(name)
        if u and cls.valid_pw(name, pw, u.pw_hash):
            return u

    @classmethod
    def make_salt(cls, length=5):
        return "".join(random.choice(letters) for x in xrange(length))

    @classmethod
    def make_pw_hash(cls, name, pw, salt=None):
        if not salt:
            salt = cls.make_salt()
        h = hashlib.sha256(name + pw + salt).hexdigest()
        return "%s,%s" % (salt, h)

    @classmethod
    def valid_pw(cls, name, password, h):
        salt = h.split(",")[0]
        return h == cls.make_pw_hash(name, password, salt)