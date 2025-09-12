import tornado.web
import tornado.ioloop

class MyHandler(tornado.web.RequestHandler):
    def get(self):
        # Retrieve signed cookie called "user"
        cookie_value = self.get_secure_cookie("user")

        if cookie_value is not None:
            self.write("Cookie value: " + cookie_value.decode())
        else:
            self.write("Cookie is not set or invalid.")

def make_app():
    return tornado.web.Application([
        (r"/", MyHandler),
    ], cookie_secret="your_secret_key")

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Listening on port 8888...")
    tornado.ioloop.IOLoop.current().start()
