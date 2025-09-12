
import tornado.web

class MyHandler(tornado.web.RequestHandler):
    def set_header(self, name, value):
        self.set_header(name, str(value))
