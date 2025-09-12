
import tornado.httpserver
import tornado.ioloop
from tornado.options import options, parse_command_line

class MyWSGIApp(object):
    def __call__(self, environ, start_response):
        # Handle the incoming request
        return ["Hello, world!"]

def main():
    app = tornado.web.Application([
        (r"/", MyWSGIApp),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
