from google.appengine.ext import db


class Like(db.Model):
    """Database model for likes.
    """
    post_id = db.StringProperty(required=True)
    username = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def by_id(cls, lid):
        """Retrieves a single like by its id.
        """
        return cls.get_by_id(int(lid))

    @classmethod
    def by_username(cls, username):
        """Retrieves all likes by a particular user, newest first.
        """
        l = cls.all().filter('username = ', username)
        if l:
            l.order("-created")
        else:
            l = None
        return l

    @classmethod
    def by_post_id(cls, pid):
        """Retrieves all likes on a particular post, newest first.
        """
        l = cls.all().filter("post_id = ", pid)
        if l:
            l.order("-created")
        else:
            l = None
        return l

    @classmethod
    def by_post_id_uid(cls, pid, uid):
        """Returns whether the a particular user has liked a particular
        post.
        """
        l = cls.all().filter("post_id = ", pid) \
            .filter("username = ", uid).get()
        return l

    @classmethod
    def by_post_id_ex_uid(cls, pid, uid):
        """Retrieves likes of a post by users other than a specified user.
        """
        l = cls.all().filter("post_id = ", pid) \
            .filter("username != ", uid)
        return l

    @classmethod
    def by_post_id_ex_uid_num(cls, pid, uid):
        """Retrieves the number of likes of a post by users other than
        a specified user.
        """
        n_l = 0
        l = cls.by_post_id_ex_uid(pid, uid)
        if l:
            for x in l:
                n_l += 1
        return n_l

    @classmethod
    def by_post_id_num(cls, pid):
        """Retrieves the number of likes of a post.
        """
        n_l = 0
        l = cls.by_post_id(pid)
        if l:
            for x in l:
                n_l += 1
        return n_l
