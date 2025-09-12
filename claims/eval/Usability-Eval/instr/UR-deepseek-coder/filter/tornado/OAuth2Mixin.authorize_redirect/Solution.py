import tornado.web
import tornado.gen
import tornado.httpclient

class OAuthHandler(tornado.web.RequestHandler):
    def initialize(self, oauth_url, client_id, redirect_uri):
        self.oauth_url = oauth_url
        self.client_id = client_id
        self.redirect_uri = redirect_uri

    def get(self):
        # Construct the authorization URL
        auth_url = f"{self.oauth_url}?client_id={self.client_id}&redirect_uri={self.redirect_uri}&response_type=code"
        
        # Redirect the user to the authorization URL
        self.redirect(auth_url)

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/oauth", OAuthHandler, dict(
            oauth_url="https://example.com/oauth/authorize",
            client_id="your_client_id",
            redirect_uri="http://your-redirect-uri"
        )),
    ])

    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
