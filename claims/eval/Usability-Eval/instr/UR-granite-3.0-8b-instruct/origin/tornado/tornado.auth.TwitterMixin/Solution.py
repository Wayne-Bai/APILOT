import tornado.web
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.auth
import tornado.options
import twitter

# Twitter API credentials
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Initialize Twitter API
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Authenticate the user
        auth = tornado.auth.TwitterAuth(self, api)
        if not auth.is_authenticated():
            self.redirect('/login')
        else:
            # Access user's Twitter account
            user = auth.get_user()
            self.write(user.screen_name)

def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
