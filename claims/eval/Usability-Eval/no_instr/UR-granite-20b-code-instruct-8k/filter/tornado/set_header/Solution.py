import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("X-Powered-By", "Tornado")
