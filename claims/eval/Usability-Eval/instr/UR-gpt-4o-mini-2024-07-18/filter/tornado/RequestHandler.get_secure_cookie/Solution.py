import tornado.web
import tornado.ioloop
import tornado.httpserver

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Example of setting a signed cookie
        self.set_secure_cookie("my_cookie", "value")

        # Getting the signed cookie
        signed_cookie = self.get_secure_cookie("my_cookie")
        if signed_cookie:
            self.write(f"Cookie value: {signed_cookie.decode()}")
        else:
            self.write("Cookie is not valid or does not exist.")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ],
    cookie_secret="your_secret_key")

if __name__ == "__main__":
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
