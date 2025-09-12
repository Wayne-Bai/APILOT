import tornado.ioloop
import tornado.web

class OAuthRedirectHandler(tornado.web.RequestHandler):
    def get(self):
        # Replace this URL with the actual OAuth authorization URL for your service
        oauth_url = "https://example.com/oauth/authorize"
        self.redirect(oauth_url)

def make_app():
    return tornado.web.Application([
        (r"/redirect", OAuthRedirectHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
