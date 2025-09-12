import tornado.ioloop
import tornado.web
import urllib.parse

class OAuthRedirectHandler(tornado.web.RequestHandler):
    def get(self):
        # Define your OAuth provider's authorization URL and parameters
        oauth_authorization_url = "https://your-oauth-provider.com/auth"
        client_id = "your_client_id"
        redirect_uri = "https://your_redirect_uri.com/callback"
        scope = "your_scope"
        
        # Build the full authorization URL
        query_params = {
            "response_type": "code",
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "scope": scope,
        }
        full_url = f"{oauth_authorization_url}?{urllib.parse.urlencode(query_params)}"
        
        # Redirect the user to the OAuth authorization URL
        self.redirect(full_url)

def make_app():
    return tornado.web.Application([
        (r"/oauth/redirect", OAuthRedirectHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server is running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
