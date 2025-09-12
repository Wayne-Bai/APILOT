
import tornado.web
import tornado.ioloop
import tornado.httpclient
import tornado.httputil

class OAuthAuthorizationHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("https://oauth.authorization.url.com")

def make_app():
    return tornado.web.Application([
        (r"/oauth/authorize", OAuthAuthorizationHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
