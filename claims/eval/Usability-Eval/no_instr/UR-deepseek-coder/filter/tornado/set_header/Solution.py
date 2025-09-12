import tornado.web

class MyHandler(tornado.web.RequestHandler):
    def set_response_header(self, name, value):
        self.set_header(name, str(value))

    def get(self):
        self.set_response_header("X-Custom-Header", "CustomValue")
        self.write("Response with custom header")

application = tornado.web.Application([
    (r"/", MyHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
