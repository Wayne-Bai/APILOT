import tornado.ioloop
import tornado.web
import tornado.auth
import tornado.escape
import os

class TwitterLoginHandler(tornado.web.RequestHandler, tornado.auth.OAuth1Mixin):
    # Define Twitter API settings
    consumer_key = "YOUR_TWITTER_CONSUMER_KEY"
    consumer_secret = "YOUR_TWITTER_CONSUMER_SECRET"
    
    @tornado.web.asynchronous
    async def get(self):
        if self.get_argument("oauth_token", None):
            # Step 2: User has been redirected to us from Twitter, complete the process
            user = await self.get_authenticated_user()
            self.write(tornado.escape.json_encode(user))
        else:
            # Step 1: Redirect user to Twitter for authentication
            self.authorize_redirect()

    async def get_authenticated_user(self):
        user = await self.oauth_get_user(self.consumer_key, self.consumer_secret)
        if user:
            return user
        else:
            raise tornado.web.HTTPError(500, "Twitter authentication failed.")

    async def authorize_redirect(self):
        """Redirects the user to obtain OAuth credentials."""
        callback = self.request.protocol + "://" + self.request.host + "/login"
        await self.authorize_redirect(consumer_key=self.consumer_key,
                                  consumer_secret=self.consumer_secret,
                                  callback_uri=callback)

def make_app():
    return tornado.web.Application([
        (r"/login", TwitterLoginHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
