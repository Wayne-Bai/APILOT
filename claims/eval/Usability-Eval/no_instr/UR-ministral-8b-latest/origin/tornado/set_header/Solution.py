import tornado.httpserver
import tornado.ioloop
import tornado.web

class MyHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header('Response-Header', 'Response-Value')
        for header_name, header_value in self.request.headers.items():
            self.set_header(header_name, str(header_value))

def make_app():
    return tornado.web.Application([
        (r"/", MyHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
