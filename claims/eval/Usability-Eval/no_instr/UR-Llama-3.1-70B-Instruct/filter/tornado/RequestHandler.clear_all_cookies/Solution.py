import tornado.ioloop
import tornado.web

class CookieHandler(tornado.web.RequestHandler):
    def get(self):
        cookie_names = [cookie_name for cookie_name in self.request.cookies.keys()]
        for cookie_name in cookie_names:
            self.clear_cookie(cookie_name)
        self.write("All cookies cleared.")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", CookieHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
