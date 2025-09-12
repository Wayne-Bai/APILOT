import tornado.web
import tornado.ioloop
import tornado.httpserver
import base64
import hmac
import hashlib

class BaseHandler(tornado.web.RequestHandler):
    COOKIE_SECRET = "YOUR_SECRET_KEY"

    def get_signed_value(self, name, value):
        signature = hmac.new(self.COOKIE_SECRET.encode(), value.encode(), hashlib.sha256).digest()
        signed_value = base64.b64encode(value.encode() + b"|" + signature).decode()
        return signed_value

    def get_secure_cookie(self, name):
        cookie = self.get_cookie(name)
        if not cookie:
            return None
        
        try:
            value, signature = base64.b64decode(cookie).rsplit(b"|", 1)
        except ValueError:
            return None
        
        expected_signature = hmac.new(self.COOKIE_SECRET.encode(), value, hashlib.sha256).digest()
        
        if hmac.compare_digest(signature, expected_signature):
            return value.decode()
        
        return None
        
class MainHandler(BaseHandler):
    def get(self):
        cookie_value = self.get_secure_cookie("my_cookie")
        if cookie_value:
            self.write(f"Retrieved signed cookie value: {cookie_value}")
        else:
            self.write("Cookie is invalid or not found")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
