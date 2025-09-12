import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def prepare(self):
        # Set a response header
        self.set_header("X-Custom-Header", str("CustomHeaderValue"))

    def get(self):
        self.write("Hello, world!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
