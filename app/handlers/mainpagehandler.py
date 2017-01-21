from app.handlers.basehandler import *


class MainPageHandler(BlogHandler):
    def get(self):
        self.write("Hello, Udacity!")
