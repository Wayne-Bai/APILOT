import tornado.ioloop
import tornado.web
import tornado.auth
import tornado.escape
import tornado.options
import tornado.httpserver

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class TwitterAuthHandler(tornado.web.RequestHandler, tornado.auth.TwitterMixin):
    @tornado.gen.coroutine
    def get(self):
        if self.get_argument("oauth_token", None):
            user = yield self.get_authenticated_user()
            # Save the user using, e.g., set_secure_cookie
            self.set_secure_cookie("user", tornado.escape.json_encode(user))
            self.redirect("/")
        else:
            yield self.authorize_redirect()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_secure_cookie("user"):
            user = tornado.escape.json_decode(self.get_secure_cookie("user"))
            self.write("Welcome, " + user["name"])
        else:
            self.write('<a href="/auth/twitter">Log in via Twitter</a>')

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/auth/twitter", TwitterAuthHandler),
    ],
    twitter_consumer_key="your_twitter_consumer_key",
    twitter_consumer_secret="your_twitter_consumer_secret",
    cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    )

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
