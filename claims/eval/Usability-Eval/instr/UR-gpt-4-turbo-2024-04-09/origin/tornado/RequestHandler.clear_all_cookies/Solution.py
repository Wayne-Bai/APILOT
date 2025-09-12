import tornado.ioloop
import tornado.web

class CookieDeleterHandler(tornado.web.RequestHandler):
    def get(self):
        # Retrieve all cookies
        cookies = self.cookies.keys()
        for name in cookies:
            self.clear_cookie(name)
        self.write("All cookies have been deleted.")

def make_app():
    return tornado.web.Application([
        (r"/delete_cookies", CookieDeleterHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Listening on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
