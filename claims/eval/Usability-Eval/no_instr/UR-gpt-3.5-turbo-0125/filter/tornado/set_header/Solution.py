
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def set_header(self, name, value):
        self.set_header(name, str(value))

    def get(self):
        self.set_header("Content-Type", "text/plain")
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
