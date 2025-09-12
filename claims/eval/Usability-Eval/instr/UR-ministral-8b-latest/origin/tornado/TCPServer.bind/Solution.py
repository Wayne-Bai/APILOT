import tornado.ioloop
import tornado.web

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server is listening on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
