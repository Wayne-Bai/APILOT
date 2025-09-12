import tornado.ioloop
import tornado.web
import tornado.auth

class TwitterAuthHandler(tornado.web.RequestHandler, tornado.auth.TwitterOAuthMixin):
    @tornado.web.asynchronous
    def get(self):
        if self.get_argument("oauth_token", None):
            self.get_authenticated_user(
                self.async_callback(self._on_auth)
            )
        else:
            self.authorize_redirect()

    def _on_auth(self, callback):
        if not callback:
            raise tornado.web.HTTPError(500, "Twitter auth failed")
        self.set_secure_cookie("user", callback["screen_name"])
        self.redirect("/")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_secure_cookie("user")
        if user:
            self.write("Hello, " + user.decode("utf-8"))
        else:
            self.write("Hello, stranger. Please <a href='/twitter'>login with Twitter</a>.")

def make_app():
    return tornado.web.Application([
        (r"/twitter", TwitterAuthHandler),
        (r"/", MainHandler),
    ], cookie_secret="YOUR_SECRET_KEY")

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
