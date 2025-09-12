import tornado.web

class DeleteCookiesHandler(tornado.web.RequestHandler):
    def get(self):
        # Retrieve all cookies and attempt to delete them
        all_cookies = self.request.cookies
        for cookie_name in all_cookies:
            self.clear_cookie(cookie_name)
        self.write("All cookies have been deleted.")
