import tornado.web

class handler(tornado.web.RequestHandler):
    def get(self):
        # Get all the cookies sent by the user
        cookies = self.request.cookies
        # Delete all the cookies
        for cookie in cookies:
            self.clear_cookie(cookie)
