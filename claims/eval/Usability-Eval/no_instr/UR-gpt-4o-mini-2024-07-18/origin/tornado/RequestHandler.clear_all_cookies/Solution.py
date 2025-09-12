import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Attempt to delete all cookies sent with this request
        for cookie in self.request.cookies:
            self.clear_cookie(cookie)

        self.write("All cookies have been deleted.")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
