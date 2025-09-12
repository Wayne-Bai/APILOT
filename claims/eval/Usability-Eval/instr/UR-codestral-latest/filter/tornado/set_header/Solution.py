import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Sets the response header 'YourHeaderName' to 'YourHeaderValue'
        self.set_header("YourHeaderName", "YourHeaderValue")
        self.write("Response with header set")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
