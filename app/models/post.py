from google.appengine.ext import db


class Post(db.Model):
    """Database model for posts.
    """
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    author = db.StringProperty(required=True)

    @classmethod
    def by_id(cls, pid):
        """Retrieves a single post by its id.
        """
        return cls.get_by_id(int(pid))

    @classmethod
    def by_username(cls, username):
        """Retrieves all comments by a particular user, newest first.
        """
        p = cls.all().filter('author = ', username)
        return p