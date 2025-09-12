import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_cookie("cookie_name", "cookie_value", expires=0)
        self.set_cookie("cookie_name", "", expires=0)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
