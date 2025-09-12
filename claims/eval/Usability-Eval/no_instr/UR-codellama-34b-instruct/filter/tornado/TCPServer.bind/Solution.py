import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)
define("address", default="localhost", help="bind to the given address", type=str)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port, address=options.address)
    tornado.ioloop.IOLoop.current().start()
