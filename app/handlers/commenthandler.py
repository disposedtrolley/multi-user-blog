from app.handlers.basehandler import *


class CommentHandler(BlogHandler):
    """Class handles comment posting.
    """
    def get(self):
        self.redirect("/blog")

    def post(self):
        """Adds a new comment to the datastore.
        """

        # keep reference to the post page for redirection later
        referrer = self.request.referer
        post_id = referrer.split("/")[-1]

        post = Post.by_id(post_id)

        comment_text = self.request.get("comment")
        self.write(comment_text)
        if comment_text:
            new_comment = Comment(post_id=post_id, username=self.user.name,
                                  comment=comment_text)
            new_comment.put()
            self.redirect(referrer)
        else:
            # TODO should render page with error
            self.redirect(referrer)


class EditCommentHandler(BlogHandler):
    """Class handles editing or deleting an existing comment.
    """
    def get(self):
        self.redirect("/blog")

    def post(self, post_id, comment_id):
        """Retrieves the user's intention and either saves or discards the edit,
        or deletes the comment.
        """
        comment = Comment.by_id(comment_id)
        if self.user and self.user.name == comment.username:
            save_clicked = self.request.get("save")
            cancel_clicked = self.request.get("cancel")
            delete_clicked = self.request.get("delete")

            edited_comment = self.request.get("comment")

            if save_clicked:
                self.save_edit(edited_comment, comment, post_id)
            elif cancel_clicked:
                self.cancel_edit(post_id)
            elif delete_clicked:
                self.delete_edit(comment, post_id)
            else:
                self.redirect("/blog")
        else:
            self.redirect("/blog")

    def save_edit(self, edited_comment, comment, post_id):
        """Overwrites the existing comment in the datastore with the edited
        version.
        """
        if edited_comment:
            comment.comment = edited_comment
            comment.put()
            self.redirect("/blog/post/%s" % post_id)
        else:
            # TODO should render page with error
            self.redirect("/blog/post/%s" % post_id)

    def cancel_edit(self, post_id):
        self.redirect("/blog/post/%s" % post_id)

    def delete_edit(self, comment, post_id):
        comment.delete()
        self.redirect("/blog/post/%s" % post_id)
