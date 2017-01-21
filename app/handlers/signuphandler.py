from app.handlers.basehandler import *


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")


def valid_username(username):
    return username and USER_RE.match(username)


def valid_password(password):
    return password and PASS_RE.match(password)


def valid_email(email):
    return not email or EMAIL_RE.match(email)


class SignupHandler(BlogHandler):
    """Class handles requests to the registration page.
    """
    def get(self):
        self.render("signup.html")

    def post(self):
        """Validates all required fields have been filled.
        """
        have_error = False
        self.username = self.request.get("username")
        self.password = self.request.get("password")
        self.verify = self.request.get("verify")
        self.email = self.request.get("email")

        params = dict(username=self.username,
                      email=self.email)

        if not valid_username(self.username):
            params["error_username"] = "Invalid username."
            have_error = True

        if not valid_password(self.password):
            params["error_password"] = "Invalid password."
            have_error = True

        elif self.password != self.verify:
            params["error_verify"] = "Passwords didn't match."
            have_error = True

        if not valid_email(self.email):
            params["error_email"] = "Invalid email address."
            have_error = True

        if have_error:
            self.render("signup.html", **params)
        else:
            self.done()

    def done(self):
        """Checks if the username is taken. If not, a new user is added to the
        datastore and the user is logged in.
        """
        u = User.by_name(self.username)
        if u:
            msg = "User already exists."
            self.render("signup.html", error_username=msg)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()

            self.login(u)
            self.redirect("/blog")
