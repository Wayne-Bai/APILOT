
import tornado.web

class HeaderHandler(tornado.web.RequestHandler):
    def set_header(self, name, value):
        self.set_header(name, str(value))
