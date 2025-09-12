import tornado.web

class CookieDeletionHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_cookie("cookie_name", "", self.request.headers.get("Cookie"))
        self.reset_cookie("cookie_name")
        self.write("Cookie deleted successfully.")

application = tornado.web.Application([
    (r"/delete_cookie", CookieDeletionHandler),
])

if __name__ == "__main__":
    application.run()
