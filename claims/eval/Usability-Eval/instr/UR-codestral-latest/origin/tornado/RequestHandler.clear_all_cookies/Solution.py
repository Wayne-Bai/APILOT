import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # delete all cookies
        for cookie in self.request.cookies:
            self.clear_cookie(cookie)
        self.write("Cookies deleted")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])
