import webapp2
import jinja2
import hmac
import os
import re
from google.appengine.ext import db

from app.models.user import User
from app.models.post import Post
from app.models.comment import Comment
from app.models.like import Like

template_dir = os.path.join(os.path.dirname(__file__), '..', "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


SECRET = "aZv=ruFTAgFAeQ?w+Wp7h"


def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)


def make_secure_val(val):
    return "%s|%s" % (val, hmac.new(SECRET, val).hexdigest())


def check_secure_val(secure_val):
    val = secure_val.split("|")[0]
    if secure_val == make_secure_val(val):
        return val


class BlogHandler(webapp2.RequestHandler):
    """Class handles general blog functionality.
    """
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        params["user"] = self.user
        return render_str(template, **params)

    def render(self, template, **kw):
        if self.user:
            self.write(self.render_str(template,
                                       auth_user=self.user.name, **kw))
        else:
            self.write(self.render_str(template, **kw))

    def set_secure_cookie(self, name, val):
        """Sets a cookie with a secure value (plaintext and hash) to the
        root of the blog.
        """
        cookie_val = make_secure_val(val)
        self.response.headers.add_header(
            "Set-Cookie",
            "%s=%s; Path=/" % (name, cookie_val))

    def read_secure_cookie(self, name):
        """Reads a cookie with a secure value (plaintext and hash) and
        returns the plaintext value, or None if the value is compromised.
        """
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)

    def initialize(self, *a, **kw):
        """Sets self.user property to the currently logged-in user. self.user
        is used elsewhere to confirm authorisation.
        """
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie("user_id")
        self.user = uid and User.by_id(int(uid))

    def login(self, user):
        """Logs the user in by setting the user cookie.
        """
        self.set_secure_cookie("user_id", str(user.key().id()))

    def logout(self):
        """Logs the user out by clearing the user cookie.
        """
        self.response.headers.add_header("Set-Cookie", "user_id=; Path=/")
