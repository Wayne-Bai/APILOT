import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def set_header(self, name, value):
        """Sets the given response header name and value"""
        super().set_header(name, value)

    def get(self):
        self.set_header('Content-Type', 'application/json')
        self.write({"message": "Hello, world!"})

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
