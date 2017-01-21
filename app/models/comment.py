from google.appengine.ext import db


class Comment(db.Model):
    """Database model for comments.
    """
    post_id = db.StringProperty(required=True)
    username = db.StringProperty(required=True)
    comment = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def by_id(cls, cid):
        """Retrieves a single comment by its id.
        """
        return cls.get_by_id(int(cid))

    @classmethod
    def by_username(cls, username):
        """Retrieves all comments by a particular user, newest first.
        """
        c = cls.all().filter('username = ', username)
        if c:
            c.order("-created")
        else:
            c = None
        return c

    @classmethod
    def by_post_id(cls, pid):
        """Retrieves all comments on a particular post, newest first.
        """
        c = cls.all().filter("post_id = ", pid)
        if c:
            c.order("-created")
        else:
            c = None
        return c
