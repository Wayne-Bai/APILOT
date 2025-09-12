import tornado.auth
import tornado.escape
import tornado.httpclient
import tornado.ioloop
import tornado.web

# Ensure you have set these environment variables
import os

class TwitterMixin(tornado.auth.OAuthMixin):
    _OAUTH_VERSION = "1.0a"
    _OAUTH_REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
    _OAUTH_AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize"
    _OAUTH_ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"
    _OAUTH_NO_CALLBACKS = False

    async def twitter_request_token(self):
        if not self.get_argument("oauth_token", True):
            self.twitter_oauth_request_token()
            return
        self.twitter_oauth_access_token()

    async def twitter_oauth_request_token(self):
        self.oauth_request_token()

    async def twitter_oauth_access_token(self):
        await self.get_authenticated_user(callback=self._on_auth)

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Twitter auth failed")
        self.set_current_user(user)
        self.redirect(self.get_argument("next", "/"))

    def set_current_user(self, user):
        if user:
            self.set_secure_cookie("user", tornado.escape.json_encode(user))
        else:
            self.clear_cookie("user")

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(TwitterMixin, BaseHandler):
    def get(self):
        if self.get_argument("oauth_token", None):
            self.twitter_request_token()
        else:
            self.render("index.html")

settings = dict(
    twitter_consumer_key=os.getenv('TWITTER_CONSUMER_KEY'),
    twitter_consumer_secret=os.getenv('TWITTER_CONSUMER_SECRET'),
    cookie_secret=os.getenv('COOKIE_SECRET'),
    debug=True,
)

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
