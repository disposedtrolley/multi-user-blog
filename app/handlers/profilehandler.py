from app.handlers.basehandler import *


class ProfileHandler(BlogHandler):
    """Class handles requests to the profile page.
    """
    def get(self, username):
        """Validates that the user exists before rendering their profile page.
        """
        if User.by_name(username):
            self.render("profile.html", username=username)
        else:
            self.redirect("/blog")
