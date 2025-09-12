import tornado.ioloop
import tornado.web

class OAuthRedirectHandler(tornado.web.RequestHandler):
    def get(self):
        client_id = "YOUR_CLIENT_ID"
        redirect_uri = "http://localhost:8888/oauth/callback"
        # Replace the URL below with the actual authorization URL for the OAuth service
        auth_url = f"https://oauthservice.com/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        self.redirect(auth_url)

def make_app():
    return tornado.web.Application([
        (r"/oauth/login", OAuthRedirectHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
