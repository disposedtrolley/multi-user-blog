from app.handlers.basehandler import *


class BlogFrontHandler(BlogHandler):
    """Class handles the home page of the blog.
    """
    def get(self):
        """Retrieves all of the posts in the datastore in descending order
        of creation date. Renders the home page with the posts.
        """
        posts = Post.all().order("-created")
        self.render("home.html", posts=posts)
