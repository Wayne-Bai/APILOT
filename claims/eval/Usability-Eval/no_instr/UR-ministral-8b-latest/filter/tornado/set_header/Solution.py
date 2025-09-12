import tornado.ioloop
import tornado.web

class ExampleHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("X-Sample-Header", "example_value")  # Setting response header

application = tornado.web.Application([
    (r"/", ExampleHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
