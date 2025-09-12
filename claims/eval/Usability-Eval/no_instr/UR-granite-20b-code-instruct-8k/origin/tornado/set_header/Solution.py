
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def set_header(self, name, value):
        self.set_header(name, value)
