import tornado.ioloop
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def set_response_header(self, name, value):
        value = str(value)
        self.set_header(name, value)

class MainHandler(BaseHandler):
    def get(self):
        self.set_response_header('Content-Type', 'text/html')
        self.write('Hello, world!')

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MainHandler),
    ])
    app.listen(8888)
    print("Serving on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
