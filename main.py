import webapp2

# import handlers
from app.handlers.basehandler import BlogHandler
from app.handlers.mainpagehandler import MainPageHandler
from app.handlers.blogfronthandler import BlogFrontHandler
from app.handlers.posthandler import PostPageHandler, NewPostHandler, EditPostHandler
from app.handlers.authhandler import LoginHandler, LogoutHandler
from app.handlers.profilehandler import ProfileHandler
from app.handlers.signuphandler import SignupHandler
from app.handlers.commenthandler import CommentHandler, EditCommentHandler
from app.handlers.likehandler import LikeHandler

# initialise app
app = webapp2.WSGIApplication([("/", MainPageHandler),
                               ("/blog/?", BlogFrontHandler),
                               ("/blog/post/([0-9]+)", PostPageHandler),
                               ("/blog/post/comment", CommentHandler),
                               ("/blog/post/([0-9]+)/comment/([0-9]+)/edit", EditCommentHandler),
                               ("/blog/post/new", NewPostHandler),
                               ("/blog/post/like", LikeHandler),
                               ("/blog/post/([0-9]+)/edit", EditPostHandler),
                               ("/blog/signup", SignupHandler),
                               ("/blog/login", LoginHandler),
                               ("/blog/logout", LogoutHandler),
                               ("/blog/profile/(\w+)", ProfileHandler)
                               ],
                              debug=True)
