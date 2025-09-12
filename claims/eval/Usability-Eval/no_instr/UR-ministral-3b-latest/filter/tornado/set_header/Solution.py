import tornado.ioloop
import tornado.web

class MyHandler(tornado.web.RequestHandler):
    def set_standard_headers(self):
        self.set_header("Content-Type", "text/html")
        self.set_header("Cache-Control", "public, max-age=0")

    def get(self):
        self.set_standard_headers()

        self.write("Hello, world")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MyHandler),
    ])

    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
