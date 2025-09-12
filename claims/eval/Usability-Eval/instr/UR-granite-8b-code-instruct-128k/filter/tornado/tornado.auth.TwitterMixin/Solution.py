import tornado.httpclient
import tornado.ioloop
import tornado.web
from tornado.auth import OAuth2Mixin
class TwitterOAuthHandler(OAuth2Mixin, tornado.web.RequestHandler):
    @tornado.web.authenticated
    def get(self):
        # Use the access token to make a request to the Twitter API
        http_client = tornado.httpclient.AsyncHTTPClient()
        response = yield http_client.fetch("https://api.twitter.com/1.1/account/verify_credentials.json",
                                            headers={"Authorization": "Bearer " + self.get_argument("access_token")})
        self.write(response.body)
settings = {
    "twitter_oauth": {
        "consumer_key": "your_consumer_key",
        "consumer_secret": "your_consumer_secret",
        "access_token_url": "https://api.twitter.com/oauth/token",
        "authorize_url": "https://api.twitter.com/oauth/authorize",
        "access_token": "your_access_token",
        "access_token_secret": "your_access_token_secret",
    }
}
application = tornado.web.Application([
    (r"/auth/twitter/callback", TwitterOAuthHandler)
], **settings)
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
