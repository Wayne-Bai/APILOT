import tornado.web
import tornado.gen
import tornado.httpclient

class OAuthHandler(tornado.web.RequestHandler):
    def get(self):
        # Define the OAuth authorization URL
        oauth_url = "https://oauth-provider.com/authorize"
        
        # Define the parameters for the OAuth request
        params = {
            "client_id": "your_client_id",
            "redirect_uri": "http://your-redirect-uri.com/callback",
            "response_type": "code",
            "scope": "your_requested_scopes"
        }
        
        # Build the full URL with parameters
        import urllib.parse
        full_url = f"{oauth_url}?{urllib.parse.urlencode(params)}"
        
        # Redirect the user to the OAuth authorization URL
        self.redirect(full_url)

def make_app():
    return tornado.web.Application([
        (r"/oauth", OAuthHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
