import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options

define("cookie_secret", default="your_secret_key", help="your secret key for signing cookies")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cookie = self.get_cookie("signed_cookie_name", secret=options.cookie_secret)
        if cookie is not None:
            self.write("The signed cookie is: " + cookie)
        else:
            self.write("The cookie is not valid or not present.")

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
