import tornado.ioloop
import tornado.web
import urllib.parse

class OAuthHandler(tornado.web.RequestHandler):
    def get(self):
        # OAuth URL
        base_url = 'https://your_service.com/oauth/authorize'

        # Your Client ID
        client_id = 'your_client_id'

        # Redirect URI
        redirect_uri = 'http://your_domain.com/callback'

        # Scope
        scope = 'read_profile'

        # Build authorization URL
        auth_url = f'{base_url}?client_id={client_id}&redirect_uri={urllib.parse.quote(redirect_uri)}&scope={scope}'

        # Redirect user for authorization
        self.redirect(auth_url)

def make_app():
    return tornado.web.Application([
        (r"/", OAuthHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
