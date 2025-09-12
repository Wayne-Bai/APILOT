import tornado.web

class DeleteCookiesHandler(tornado.web.RequestHandler):
    def get(self):
        # Get the cookies sent with the request
        cookies = self.request.cookies
        
        # Iterate over the cookies and delete each one
        for cookie in cookies:
            self.clear_cookie(cookie.key)
        
        # Redirect the user to the home page
        self.redirect("/")
