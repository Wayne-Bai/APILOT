import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Server running on port 8888")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888, address='127.0.0.1')
    print("Server running on port 8888")
    tornado.ioloop.IOLoop.current().start()
