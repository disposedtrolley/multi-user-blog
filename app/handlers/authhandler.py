from app.handlers.basehandler import *


class LoginHandler(BlogHandler):
    """Class handles requests to the Login page.
    """
    def get(self):
        self.render("login.html")

    def post(self):
        """Authenticates the user based on the provided username and password.
        Directs the user to the main page if successful, and presents an
        error message otherwise.
        """
        username = self.request.get("username")
        password = self.request.get("password")

        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect("/blog")
        else:
            msg = "Invalid login"
            self.render("login.html", error=msg)


class LogoutHandler(BlogHandler):
    """Class handles requests to the Logout page.
    """
    def get(self):
        self.logout()
        self.redirect("/blog")