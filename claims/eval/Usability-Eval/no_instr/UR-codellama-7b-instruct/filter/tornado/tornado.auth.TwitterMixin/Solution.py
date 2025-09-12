
import tornado.httpclient
import tornado.auth

# Set up Tornado OAuth client
twitter_consumer_key = 'your_consumer_key'
twitter_consumer_secret = 'your_consumer_secret'
oauth_callback_url = 'https://your_server/callback'
oauth_client = tornado.auth.OAuth2Client(
    client_id=twitter_consumer_key,
    client_secret=twitter_consumer_secret,
    redirect_uri=oauth_callback_url,
    scope='',
)
