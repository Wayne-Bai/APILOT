
import tornado

class SetHeaderHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "text/plain")
