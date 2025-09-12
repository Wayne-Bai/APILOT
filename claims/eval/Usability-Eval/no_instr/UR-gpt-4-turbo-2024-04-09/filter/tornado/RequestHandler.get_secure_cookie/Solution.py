import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cookie_name = "user"
        signed_value = self.get_secure_cookie(cookie_name)
        if signed_value:
            self.write(f"Welcome back! Cookie value: {signed_value.decode()}")
        else:
            self.write("Cookie doesn't exist or is invalid.")

def make_app():
    settings = {
        'cookie_secret': 'YOUR_SECRET_KEY_HERE',
    }
    return tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
