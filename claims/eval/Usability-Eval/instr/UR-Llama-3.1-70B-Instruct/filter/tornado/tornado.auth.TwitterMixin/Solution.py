import tornado.auth
import tornado.ioloop
import tornado.web
import tornado.gen

class TwitterAuthHandler(tornado.web.RequestHandler, tornado.auth.TwitterMixin):
    @tornado.gen.coroutine
    def get(self):
        if self.get_argument('oauth_token', None):
            self.finish('<html><body>Your are signed in. Check terminal</body></html>')
            access_token = yield self.get_authenticated_user(
                redirect_uri='http://localhost:8000/auth',
                client_id=self.application.settings['twitter_consumer_key'],
                client_secret=self.application.settings['twitter_consumer_secret'],
                callback=self.save_user_info
            )
        else:
            yield self.authorize_redirect(
                redirect_uri='http://localhost:8000/auth',
                client_id=self.application.settings['twitter_consumer_key'],
                client_secret=self.application.settings['twitter_consumer_secret'],
            )

    def save_user_info(self, user):
        if not user:
            self.clear_cookie("user")
        else:
            print(user)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class Application(tornado.web.Application):
    def __init__(self):
        settings = {
            'template_path': 'templates',
           'static_path':'static',
            'twitter_consumer_key': 'your consumer key',
            'twitter_consumer_secret': 'your consumer secret',
            'xsrf_cookies': True,
            'cookie_secret': 'your secret key',
            'login_url': '/auth',
        }

        handlers = [
            (r"/", IndexHandler),
            (r"/auth", TwitterAuthHandler),
        ]

        super(Application, self).__init__(handlers, **settings)


if __name__ == "__main__":
    app = Application()
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
