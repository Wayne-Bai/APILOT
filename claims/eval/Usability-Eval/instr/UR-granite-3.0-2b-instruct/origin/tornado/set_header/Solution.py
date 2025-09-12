from tornado import web

class MainHandler(web.RequestHandler):
    def set_header(self, name, value):
        self.set_header(name, str(value))
