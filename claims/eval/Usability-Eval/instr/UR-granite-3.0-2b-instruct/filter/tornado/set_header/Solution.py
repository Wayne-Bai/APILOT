import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def set_header(self, name, value):
        self.set_header(name, str(value))

def create_application():
    return tornado.web.Application([
        (r'/', MainHandler),
    ])
