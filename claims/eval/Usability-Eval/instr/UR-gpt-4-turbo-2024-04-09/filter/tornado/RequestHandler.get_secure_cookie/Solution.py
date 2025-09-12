import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cookie_name = "your_cookie_name"
        signed_cookie = self.get_secure_cookie(cookie_name)
        if signed_cookie:
            self.write(f"Cookie value: {signed_cookie.decode()}")
        else:
            self.write("No valid cookie found.")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
