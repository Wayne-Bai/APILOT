import tornado.web
from tornado.ioloop import IOLoop

class SignCookie(tornado.web.RequestHandler):
    def get(self):
        # Sign the cookie with a secret key
        signed_cookie = self.sign_cookie("secret_key")
        self.set_cookie(signed_cookie)

def make_app():
    return tornado.web.Application([
        (r"/sign_cookie", SignCookie),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    IOLoop.current().run_until_complete(app)
