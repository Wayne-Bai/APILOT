import tornado.ioloop
import tornado.web
import tornado.auth
import tornado.gen

class TwitterLoginHandler(tornado.web.RequestHandler, tornado.auth.OAuth2Mixin):
    _OAUTH_ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"
    _OAUTH_AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize"
    _OAUTH_REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
    
    def initialize(self, twitter_consumer_key, twitter_consumer_secret):
        self.twitter_consumer_key = twitter_consumer_key
        self.twitter_consumer_secret = twitter_consumer_secret

    @tornado.gen.coroutine
    def get(self):
        if self.get_argument("oauth_token", None):
            user = yield self.get_authenticated_user()
            # Save the user using a database or session
            self.write(user)
        else:
            yield self.authorize_redirect(callback_uri=self.request.full_url())
    
    @tornado.gen.coroutine
    def get_authenticated_user(self):
        user_info = yield self.oauth2_access_token(self.twitter_consumer_key, self.twitter_consumer_secret)
        return user_info

def make_app(twitter_consumer_key, twitter_consumer_secret):
    return tornado.web.Application([
        (r"/auth/login", TwitterLoginHandler, dict(
            twitter_consumer_key=twitter_consumer_key,
            twitter_consumer_secret=twitter_consumer_secret
        )),
    ], debug=True)

if __name__ == "__main__":
    twitter_consumer_key = 'YOUR_CONSUMER_KEY'
    twitter_consumer_secret = 'YOUR_CONSUMER_SECRET'
    
    app = make_app(twitter_consumer_key, twitter_consumer_secret)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
