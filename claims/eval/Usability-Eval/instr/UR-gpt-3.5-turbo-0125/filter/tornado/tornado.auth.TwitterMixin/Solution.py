
import tornado.web
import tornado.ioloop
import tornado.auth

class TwitterAuthHandler(tornado.web.RequestHandler, tornado.auth.TwitterMixin):
    async def get(self):
        if self.get_argument("oauth_token", None):
            user = await self.get_authenticated_user()
            # Do something with the authenticated user, like storing it in a database
            self.write("Authenticated user: {}".format(user))
        else:
            await self.authorize_redirect(callback_uri="YOUR_CALLBACK_URL")

def make_app():
    return tornado.web.Application([
        (r"/auth/twitter", TwitterAuthHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
