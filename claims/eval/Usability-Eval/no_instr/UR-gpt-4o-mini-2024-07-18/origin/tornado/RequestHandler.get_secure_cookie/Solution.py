import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        signed_cookie = self.get_secure_cookie("my_cookie")
        if signed_cookie:
            self.write(f"Valid signed cookie: {signed_cookie.decode()}")
        else:
            self.write("No valid signed cookie.")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], cookie_secret="YOUR_SECRET_KEY")

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
