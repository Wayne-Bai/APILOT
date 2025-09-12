import tornado.web

class MyHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("X-Custom-Header", "Custom Value")
