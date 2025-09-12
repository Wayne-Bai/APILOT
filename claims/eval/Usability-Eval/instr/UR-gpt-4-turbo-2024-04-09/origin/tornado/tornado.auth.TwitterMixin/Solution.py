import tornado.web
import tornado.ioloop
import tornado.httpclient
import tornado.auth
import os

class TwitterAuthHandler(tornado.web.RequestHandler, tornado.auth.TwitterMixin):
    @tornado.gen.coroutine
    def get(self):
        if self.get_argument("oauth_token", None):
            user_info = yield self.get_authenticated_user()
            if user_info:
                self.write(f"Authenticated user: {user_info['username']}")
                self.finish()
        else:
            yield self.authenticate_redirect()
            
def make_app():
    return tornado.web.Application([
        (r"/auth/twitter", TwitterAuthHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
