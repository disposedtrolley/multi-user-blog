from app.handlers.basehandler import *


class LikeHandler(BlogHandler):
    """Class handles post liking.
    """
    def get(self):
        self.redirect("/blog")

    def post(self):
        """Toggles between liking and not liking a post by adding and
        deleting a Like record from the datastore.
        """
        referrer = self.request.referer
        post_id = referrer.split("/")[-1]

        # if existing like, delete like from db
        like = Like.by_post_id_uid(post_id, self.user.name)
        if like:
            like.delete()
        else:
            # add Like to database
            new_like = Like(username=self.user.name,
                            post_id=post_id)
            new_like.put()
        self.redirect(referrer)
