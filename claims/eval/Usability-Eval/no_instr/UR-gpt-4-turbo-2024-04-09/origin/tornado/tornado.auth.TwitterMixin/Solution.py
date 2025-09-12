import tornado.web
import tornado.ioloop
import tornado.httpclient
import tornado.auth
import os
import urllib.parse

class TwitterOAuth2LoginHandler(tornado.web.RequestHandler, tornado.auth.OAuth2Mixin):
    _OAUTH_AUTHORIZE_URL = "https://twitter.com/i/oauth2/authorize"
    _OAUTH_ACCESS_TOKEN_URL = "https://api.twitter.com/oauth2/token"
    _OAUTH_NO_CALLBACKS = False
    _OAUTH_SETTINGS_KEY = 'twitter_oauth'

    async def get(self):
        if self.get_argument('code', False):
            user = await self.get_authenticated_user(
                redirect_uri=self.settings[self._OAUTH_SETTINGS_KEY]['redirect_uri'],
                client_id=self.settings[self._OAUTH_SETTINGS_KEY]['client_id'],
                client_secret=self.settings[self._OAUTH_SETTINGS_KEY]['client_secret'],
                code=self.get_argument('code')
            )
            # Save the user with e.g. self.current_user = user
            self.finish(user)
        else:
            await self.authorize_redirect(
                redirect_uri=self.settings[self._OAUTH_SETTINGS_KEY]['redirect_uri'],
                client_id=self.settings[self._OAUTH_SETTINGS_KEY]['client_id'],
                scope=['tweet.read', 'users.read', 'follows.read', 'offline.access'],
                response_type='code'
            )

def make_app():
    settings = {
        "twitter_oauth": {
            "client_id": os.environ.get("TWITTER_CONSUMER_KEY"),
            "client_secret": os.environ.get("TWITTER_CONSUMER_SECRET"),
            "redirect_uri": 'http://yourwebsite.com/auth/twitter',
        },
    }
    return tornado.web.Application([
        (r"/auth/twitter", TwitterOAuth2LoginHandler),
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
