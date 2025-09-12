
from tornado import web

class Handler(web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/html")
        self.write("<h1>Hello, world!</h1>")
