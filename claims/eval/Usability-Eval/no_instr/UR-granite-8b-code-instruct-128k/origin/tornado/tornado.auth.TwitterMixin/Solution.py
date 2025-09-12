import tornado.web
import tornado.ioloop
import tornado.httpclient
import tornado.auth

class TwitterHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_argument('code', False):
            # Make sure you have a Consumer Key and Secret
            # from Twitter Developer Portal
            self.get_authenticated_user(
                redirect_uri='http://yourwebsite.com/auth/twitter',
                client_id=YOUR_CLIENT_ID,
                client_secret=YOUR_CLIENT_SECRET,
                code=self.get_argument('code'))
            self.finish("Authentication successful!")
        else:
            self.authorize_redirect(
                redirect_uri='http://yourwebsite.com/auth/twitter',
                client_id=YOUR_CLIENT_ID,
                scope=['email'])

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/auth/twitter", TwitterHandler),
    ])
    application.listen(8000)
    tornado.ioloop.IOLoop.current().start()
