import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, this is a Tornado web server!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888, address='127.0.0.1')  # Bind server to port 8888 on localhost
    tornado.ioloop.IOLoop.current().start()
