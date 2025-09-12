import tornado.ioloop
import tornado.web

class CookieSigner(tornado.web.RequestHandler):
    def get(self):
        # Sign and timestamp the cookie
        self.set_secure_cookie("name", "value", secure=True, httponly=True)
        self.write("Cookie signed and timestampped!")
