import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler
import hashlib
import hmac
import time
import base64
import os

# Secret key for HMAC, don't share this in production
SECRET_KEY = os.urandom(32)

def create_signed_value(secret_key, name, value):
    """Creates a signed value for a cookie using HMAC"""
    timestamp = str(int(time.time()))
    value_to_sign = f"{name}|{value}|{timestamp}"
    signature = base64.b64encode(hmac.new(secret_key, value_to_sign.encode('utf-8'), hashlib.sha256).digest())
    signed_value = f"{value}|{timestamp}|{signature.decode('utf-8')}"
    return signed_value

def verify_signed_value(secret_key, name, signed_value, max_age_days=1):
    """Verifies the signed value of a cookie"""
    try:
        value, timestamp, signature = signed_value.split('|')
        if int(time.time()) - int(timestamp) > max_age_days * 86400:
            return None  # Expired
        expected_signature = base64.b64encode(hmac.new(secret_key, f"{name}|{value}|{timestamp}".encode('utf-8'), hashlib.sha256).digest())
        if hmac.compare_digest(signature.encode('utf-8'), expected_signature):
            return value
        else:
            return None
    except Exception:
        return None

class MainHandler(RequestHandler):
    def get(self):
        # Create and set a signed cookie
        signed_value = create_signed_value(SECRET_KEY, "user_id", "123456")
        self.set_cookie("user_id", signed_value)
        self.write("Cookie has been set!")

    def post(self):
        # Verify the signed cookie
        signed_value = self.get_cookie("user_id")
        if signed_value:
            user_id = verify_signed_value(SECRET_KEY, "user_id", signed_value)
            if user_id:
                self.write(f"Verified user ID: {user_id}")
            else:
                self.write(f"Invalid or expired cookie!")
        else:
            self.write("No cookie found!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
