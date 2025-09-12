import tornado.web

class OAuthAuthorizationHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("https://example.com/oauth/authorize")
