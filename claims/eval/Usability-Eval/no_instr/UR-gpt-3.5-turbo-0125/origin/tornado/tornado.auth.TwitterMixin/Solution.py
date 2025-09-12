
import tornado.web
import tornado.httpclient
import tornado.gen
import urllib.parse
import hmac
import hashlib
import base64
import time

class TwitterOAuthHandler(tornado.web.RequestHandler):

    consumer_key = "YOUR_CONSUMER_KEY"
    consumer_secret = "YOUR_CONSUMER_SECRET"
    request_token_url = "https://api.twitter.com/oauth/request_token"
    authorize_url = "https://api.twitter.com/oauth/authorize"
    access_token_url = "https://api.twitter.com/oauth/access_token"

    def get_auth_header(self, method, url, params):
        oauth_params = {
            'oauth_consumer_key': self.consumer_key,
            'oauth_nonce': str(time.time()),
            'oauth_signature_method': "HMAC-SHA1",
            'oauth_timestamp': str(int(time.time())),
            'oauth_version': "1.0"
        }
        oauth_params.update(params)

        # Construct base string
        base_string = "&".join([method.upper(),
                                urllib.parse.quote(url, safe=''), 
                                urllib.parse.quote('&'.join([f"{k}={v}" for k, v in sorted(oauth_params.items())]), safe='')])

        # Construct signing key
        signing_key = "&".join([self.consumer_secret, ""])

        # Construct signature
        signature = base64.b64encode(hmac.new(signing_key.encode(), base_string.encode(), hashlib.sha1).digest())

        oauth_params['oauth_signature'] = signature.decode()

        return ', '.join([f'{k}="{v}"' for k, v in oauth_params.items()])

    async def get(self):
        oauth_params = {
            'oauth_callback': 'http://localhost:8888/oauth_complete',
            'oauth_signature': ""
        }
        auth_header = self.get_auth_header('GET', self.request_token_url, oauth_params)

        response = await tornado.httpclient.AsyncHTTPClient().fetch(self.request_token_url, headers={'Authorization': f"OAuth {auth_header}"})
        self.write(response.body)

def make_app():
    return tornado.web.Application([
        (r"/twitter_oauth", TwitterOAuthHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
