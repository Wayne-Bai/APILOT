import tornado.ioloop
import tornado.web
import tornado.auth
import tornado.gen

# Replace these with your Twitter app's keys
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<a href="/login/twitter">Login with Twitter</a>')

class TwitterLoginHandler(tornado.web.RequestHandler, tornado.auth.TwitterMixin):
    @tornado.gen.coroutine
    def get(self):
        yield self.authorize_redirect(
            redirect_uri=self.request.protocol + "://" + self.request.host + "/login/twitter/authorized",
            client_id=CONSUMER_KEY,
            client_secret=CONSUMER_SECRET
        )

class TwitterAuthorizedHandler(tornado.web.RequestHandler, tornado.auth.TwitterMixin):
    @tornado.gen.coroutine
    def get(self):
        user = yield self.get_authenticated_user()
        if not user:
            self.redirect('/')
            return

        self.set_secure_cookie("user", user['screen_name'])
        self.write("Hello, " + user['screen_name'])

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login/twitter", TwitterLoginHandler),
        (r"/login/twitter/authorized", TwitterAuthorizedHandler),
    ],
    cookie_secret="YOUR_SECRET_KEY",  # Replace with a random secret
    login_url="/")

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
