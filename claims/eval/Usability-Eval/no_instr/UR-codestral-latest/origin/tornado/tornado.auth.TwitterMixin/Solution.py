Python
import tornado.web
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class TwitterLoginHandler(tornado.web.RequestHandler, tornado.auth.TwitterMixin):
    @tornado.gen.coroutine
    def get(self):
        if self.get_argument('oauth_token', None):
            user = yield self.get_authenticated_user()
            self.set_secure_cookie('user', tornado.escape.json_encode(user))
            self.redirect('/')
        else:
            yield self.authorize_redirect()

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r'/auth/twitter', TwitterLoginHandler),]
        settings = {"twitter_consumer_key": "YOUR_CONSUMER_KEY",
                    "twitter_consumer_secret": "YOUR_CONSUMER_SECRET"}
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
