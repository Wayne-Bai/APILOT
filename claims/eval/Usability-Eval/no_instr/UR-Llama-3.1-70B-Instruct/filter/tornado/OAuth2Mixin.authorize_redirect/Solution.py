import tornado.ioloop
import tornado.web
import tornado.escape
import tornado.auth
import urllib.parse

class AuthLoginHandler(tornado.web.RequestHandler, tornado.auth.GoogleOAuth2Mixin):
    async def get(self):
        if self.get_argument('code', False):
            user = await self.get_authenticated_user(redirect_uri='your_redirect_url',
                                                     code=self.get_argument('code'))
            # Save the user data
            self.set_secure_cookie("user", tornado.escape.json_encode(user))
            self.redirect('/next-page')
            return

        await self.authorize_redirect(
            redirect_uri='your_redirect_url',
            client_id='your_client_id',
            scope=['email'],
            response_type='code',
            extra_params={'access_type': 'offline'})

class NextPageHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_secure_cookie("user")
        if user:
            self.write('Welcome,'+ tornado.escape.json_decode(user)['email'])
        else:
            self.write('You are not logged in')

if __name__ == "__main__":
    settings = {
        "template_path": "./templates",
        "static_path": "./static",
        "debug": True,
        "cookie_secret": "your_cookie_secret",
        "login_url": "/auth/login",
    }
    app = tornado.web.Application(
        [
            (r'/auth/login', AuthLoginHandler),
            (r'/next-page', NextPageHandler),
        ],
        **settings
    )
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
