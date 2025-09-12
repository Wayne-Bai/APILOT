import tornado.ioloop
import tornado.web
import tornado.gen
import webbrowser

class OAuthRedirectHandler(tornado.web.RequestHandler):
    def get(self):
        # URL for the OAuth authorization request
        client_id = "YOUR_CLIENT_ID"
        redirect_uri = "YOUR_REDIRECT_URI"
        authorization_url = f"https://authorization.server/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"

        # Redirect the user to the OAuth authorization URL
        self.redirect(authorization_url)

def make_app():
    return tornado.web.Application([
        (r"/oauth/redirect", OAuthRedirectHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server is listening on http://localhost:8888/oauth/redirect")
    tornado.ioloop.IOLoop.current().start()
