import tornado.web
import tornado.ioloop
from tornado.options import options

class OAuthRedirectHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Redirecting to OAuth authorization URL")
        self.redirect("https://example.com/oauth/authorize?response_type=code&client_id=your_client_id&redirect_uri=your_redirect_uri&scope=your_scope")

if __name__ == '__main__':
    options.parse_command_line()
    application = tornado.web.Application([
        (r"/", OAuthRedirectHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().run_until_complete(application)
