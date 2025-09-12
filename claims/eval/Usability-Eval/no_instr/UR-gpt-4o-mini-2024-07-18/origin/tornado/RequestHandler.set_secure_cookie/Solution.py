import tornado.ioloop
import tornado.web
import tornado.escape
import time
import hashlib
import hmac
import base64

SECRET_KEY = 'your_secret_key'  # Replace with your secret key

def sign_cookie(cookie_value):
    """Signs the cookie value with a secret key."""
    signature = hmac.new(SECRET_KEY.encode(), cookie_value.encode(), hashlib.sha256).digest()
    signed_cookie = f"{cookie_value}.{base64.urlsafe_b64encode(signature).decode()}"
    return signed_cookie

def verify_cookie(signed_cookie):
    """Verifies the signed cookie."""
    try:
        value, signature = signed_cookie.rsplit('.', 1)
        expected_signature = hmac.new(SECRET_KEY.encode(), value.encode(), hashlib.sha256).digest()
        return base64.urlsafe_b64encode(expected_signature).decode() == signature
    except Exception:
        return False

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Set a signed cookie
        cookie_value = "user_id=12345;timestamp=" + str(int(time.time()))
        signed_cookie = sign_cookie(cookie_value)
        self.set_cookie("my_cookie", signed_cookie)
        self.write("Cookie set.")

    def post(self):
        # Retrieve and verify the signed cookie
        signed_cookie = self.get_cookie("my_cookie")
        if signed_cookie and verify_cookie(signed_cookie):
            self.write("Cookie verified: " + signed_cookie)
        else:
            self.write("Invalid cookie.")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
