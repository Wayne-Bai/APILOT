import tornado.ioloop
import tornado.web
import tornado.auth
import tornado.httpclient

class TwitterLoginHandler(tornado.web.RequestHandler, tornado.auth.TwitterMixin):
    @tornado.gen.coroutine
    def get(self):
        if self.get_argument('oauth_token', None):
            user = yield self.get_authenticated_user()
            self.set_secure_cookie('user', tornado.escape.json_encode(user))
            self.redirect('/')
        else:
            yield self.twitter_request(
                'request_token',
                '/auth/twitter',
                self.async_callback(self._on_auth)
            )

    def _on_auth(self, response):
        if not response:
            self.clear_all_cookies()
            raise tornado.web.HTTPError(500, 'Twitter authentication failed')

        self.redirect(self.authorize_url(response['oauth_token']))

class HomeHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user_json = self.get_secure_cookie('user')
        if not user_json:
            return None
        return tornado.escape.json_decode(user_json)

    @tornado.web.authenticated
    def get(self):
        self.write('Welcome, %s!' % self.current_user['name'])

application = tornado.web.Application([
    (r'/', HomeHandler),
    (r'/auth/twitter', TwitterLoginHandler),
], twitter_consumer_key='YOUR_CONSUMER_KEY', twitter_consumer_secret='YOUR_CONSUMER_SECRET')

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
