import tornado.web
from tornado.wsgi import WSGIContainer

class HelloWorldHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", HelloWorldHandler),
    ])
    container = WSGIContainer(app)
    server = tornado.httpserver.HTTPServer(container)
    server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
