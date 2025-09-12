import tornado
from tornado import web
import time
import hashlib
import hmac
import base64
import json

# Generate a secret key for signing and verifying cookies
secret_key = b"my_secret_key"

# Function to generate a signed cookie
def generate_signed_cookie(cookie_name, cookie_value):
    timestamp = str(int(time.time()))
    signature = hmac.new(secret_key, cookie_name.encode() + cookie_value.encode() + timestamp.encode(), hashlib.sha256).digest()
    signature = base64.b64encode(signature).decode()
    return f"{cookie_value}:{timestamp}:{signature}"

# Function to verify a signed cookie
def verify_signed_cookie(cookie_name, cookie_value):
    parts = cookie_value.split(":")
    if len(parts)!= 3:
        return False
    value, timestamp, signature = parts
    expected_signature = hmac.new(secret_key, cookie_name.encode() + value.encode() + timestamp.encode(), hashlib.sha256).digest()
    expected_signature = base64.b64encode(expected_signature).decode()
    return signature == expected_signature

class MainHandler(web.RequestHandler):
    def get(self):
        # Generate a signed cookie
        cookie_value = json.dumps({"user_id": 123})
        signed_cookie = generate_signed_cookie("user", cookie_value)
        self.set_secure_cookie("user", signed_cookie)

    def post(self):
        # Verify a signed cookie
        cookie_value = self.get_secure_cookie("user")
        if cookie_value and verify_signed_cookie("user", cookie_value.decode()):
            self.write("Cookie is valid")
        else:
            self.write("Cookie is invalid")

if __name__ == "__main__":
    settings = {
        "cookie_secret": secret_key,
    }
    application = web.Application([
        (r"/", MainHandler),
    ], **settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
