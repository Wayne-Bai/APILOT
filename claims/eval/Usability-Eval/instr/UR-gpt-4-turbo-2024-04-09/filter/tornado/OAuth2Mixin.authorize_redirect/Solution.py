import tornado.ioloop
import tornado.web

class OAuthRedirectHandler(tornado.web.RequestHandler):
    def get(self):
        # Replace these with your service's specific details
        client_id = 'YOUR_CLIENT_ID'
        redirect_uri = 'YOUR_REDIRECT_URI'
        scope = 'email'

        # Constructing the authorization URL
        # Replace 'YOUR_AUTHORIZATION_ENDPOINT' with your OAuth service's authorization endpoint
        authorization_url = f"https://YOUR_AUTHORIZATION_ENDPOINT?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"

        # Redirect the user to the OAuth service's authorization URL
        self.redirect(authorization_url)

def make_app():
    return tornado.web.Application([
        (r"/auth", OAuthRedirectHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server is running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
