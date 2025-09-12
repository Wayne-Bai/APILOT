import tornado.ioloop
import tornado.web
import tweepy

consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
callback_uri = 'your_callback_uri'

class TwitterHandler(tornado.web.RequestHandler):
    def get(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
        try:
            redirect_url = auth.get_authorization_url()
            self.redirect(redirect_url)
        except tweepy.TweepError:
            print('Error! Failed to get request token.')

application = tornado.web.Application([
    (r"/twitter", TwitterHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
