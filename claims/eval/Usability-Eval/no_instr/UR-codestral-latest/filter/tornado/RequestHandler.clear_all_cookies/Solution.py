import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        for cookie_name in self.request.cookies:
            self.clear_cookie(cookie_name)
        self.write("All cookies deleted")
