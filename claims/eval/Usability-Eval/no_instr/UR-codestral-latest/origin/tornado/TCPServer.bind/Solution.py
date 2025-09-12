import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888, address="127.0.0.1")  # replace 8888 with your port number and "127.0.0.1" with your IP address
    tornado.ioloop.IOLoop.current().start()
