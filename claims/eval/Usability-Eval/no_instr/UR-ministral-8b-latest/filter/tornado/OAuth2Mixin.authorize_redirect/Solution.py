import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # This is the URL you need to redirect to for OAuth authorize.
        oauth_url = "https://oauth.provider.com/auth?client_id=your_client_id&response_type=code&redirect_uri=http://your.callback_uri"

        # Redirect user to the OAuth authorization URL
        self.redirect(oauth_url)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
