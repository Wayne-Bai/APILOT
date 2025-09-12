import tornado.ioloop
import tornado.web
import tornado.httpclient
import urllib.parse

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Replace these with your OAuth client details
        client_id = 'YOUR_CLIENT_ID'
        redirect_uri = 'YOUR_REDIRECT_URI'
        authorization_base_url = 'https://oauth.example.com/authorize'

        # Construct the redirect URL with necessary query parameters
        params = {
            'client_id': client_id,
            'redirect_uri': redirect_uri,
            'response_type': 'code',  # We're asking for the authorization code
            'scope': 'read write',   # Example scopes
        }
        
        auth_url = f"{authorization_base_url}?{urllib.parse.urlencode(params)}"
        
        # Redirect user to OAuth login page
        self.redirect(auth_url)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server is running at http://localhost:8888/")
    tornado.ioloop.IOLoop.current().start()
