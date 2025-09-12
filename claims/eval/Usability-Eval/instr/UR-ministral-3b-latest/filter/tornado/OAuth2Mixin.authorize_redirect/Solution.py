import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.escape import json_decode

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        # Redirect to OAuth authorization URL
        self.redirect("https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=YOUR_OAUTH_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI&scope=email")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", HomeHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
