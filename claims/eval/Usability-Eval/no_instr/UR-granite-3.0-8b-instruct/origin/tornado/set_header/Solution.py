import tornado.web

class YourHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("X-Custom-Header", "Your Value")
