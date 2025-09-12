import tornado.ioloop
import tornado.web
from tornado.wsgi import WSGIContainer

def hello_world():
    return "Hello, World!"

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(hello_world())

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ], debug=True)

    tornado.ioloop.IOLoop.current().start()
