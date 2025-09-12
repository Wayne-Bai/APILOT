
import tornado.web
from tornado.wsgi import WSGIApplication

class MyWSGIApplication(WSGIApplication):
    def __init__(self):
        self.routes = [
            (r"/", IndexHandler),
            (r"/about", AboutHandler)
        ]

        super().__init__(routes=self.routes)

if __name__ == "__main__":
    tornado.web.Application([(r"/", MyWSGIApplication)])
