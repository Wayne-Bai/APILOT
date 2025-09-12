
import tornado.web

class OAuthRedirectHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # Redirects the user to obtain OAuth authorization for this service
        redirect_url = "https://www.example.com/oauth2/authorize"
        self.redirect(redirect_url)
