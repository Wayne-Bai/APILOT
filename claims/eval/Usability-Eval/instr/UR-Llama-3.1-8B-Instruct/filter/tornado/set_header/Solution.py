import tornado.web
import tornado.httpclient

class CustomHeaderHandler(tornado.web.RequestHandler):
    def head(self):
        self.set_header('Custom-Header', 'Custom Header Value')
        self.finish()

    def get(self):
        self.set_header('Custom-Header', 'Custom Header Value')
        self.write('Hello, world!')

def make_app():
    return tornado.web.Application([
        (r"/", CustomHeaderHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
