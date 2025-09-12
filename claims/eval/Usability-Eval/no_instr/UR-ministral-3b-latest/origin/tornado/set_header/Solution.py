from tornado.web import RequestHandler

class MyHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("My-Header", "MyHeaderValue")

    def get(self):
        self.write("Got the request")

app = tornado.web.Application([(r'/', MyHandler)])
app.listen(8888)

tornado.ioloop.IOLoop.current().start()
