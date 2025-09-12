import tornado.web
import tornado.ioloop
from tornado.options import options

class OAuthRedirectHandler(tornado.web.RequestHandler):
    def get(self):
        # Set the OAuth authorization URL
        oauth_url = "https://example.com/oauth/authorize?response_type=code&client_id=your_client_id&redirect_uri=your_redirect_uri"
        self.write(oauth_url)

def make_app():
    return tornado.web.Application([
        (r"/", OAuthRedirectHandler),
    ])

if __name__ == '__main__':
    options.parse_command_line()
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().run_until_complete(app)
    tornado.ioloop.IOLoop.current().run_until_complete(app.wait_and_terminate())
