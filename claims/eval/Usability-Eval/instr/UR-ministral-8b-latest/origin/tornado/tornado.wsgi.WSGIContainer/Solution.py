import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

import wsgiref
from wsgiref.simple_server import WSGIRequestHandler

# Define command line options
define("port", default=8888, help="run on the given port", type=int)

# Handle WSGI requests with Tornado HTTP server
class WSGIRequestHandler(WSGIRequestHandler):
    def log_request(self, exc_info=None):
        self.finish("Handling WSGI request")

class CustomRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Welcome to WSGI-compatible Tornado server!")

    def post(self):
        self.set_status(201)
        self.write("Created")

def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [b"Hello from WSGI application!"]

def make_app():
    return tornado.web.Application([
        (r"/ acostumado", CustomRequestHandler),
    ])

def main():
    parse_command_line()
    app = make_app()

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)

    print(f"WSGI-compatible Tornado HTTP server is running on http://localhost:{options.port}")
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
