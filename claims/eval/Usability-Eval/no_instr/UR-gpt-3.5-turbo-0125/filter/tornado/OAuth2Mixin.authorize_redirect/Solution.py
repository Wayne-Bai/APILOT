
import tornado.web

class OAuthHandler(tornado.web.RequestHandler):
    def get(self):
        # Code to redirect user to OAuth authorization URL
        self.redirect("https://oauth.authorization.url")
