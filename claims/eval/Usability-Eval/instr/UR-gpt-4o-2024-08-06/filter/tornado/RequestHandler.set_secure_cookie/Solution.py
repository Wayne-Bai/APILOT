import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler
import time
import hmac
import hashlib
import base64

SECRET_KEY = 'your_secret_key_here'

def create_signed_value(secret, name, value):
    timestamp = str(int(time.time()))
    value = base64.b64encode(value.encode('utf-8')).decode('utf-8')
    signature = hmac.new(secret.encode('utf-8'), f"{name}{value}{timestamp}".encode('utf-8'), hashlib.sha256).hexdigest()
    return f"{value}|{timestamp}|{signature}"

def verify_signed_value(secret, name, signed_value):
    try:
        value, timestamp, signature = signed_value.split('|')
        expected_signature = hmac.new(secret.encode('utf-8'), f"{name}{value}{timestamp}".encode('utf-8'), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(signature, expected_signature):
            return None
        return base64.b64decode(value).decode('utf-8')
    except Exception as e:
        return None

class MainHandler(RequestHandler):
    def get(self):
        # Sign and set cookie
        signed_value = create_signed_value(SECRET_KEY, 'cookie_name', 'cookie_value')
        self.set_cookie("mycookie", signed_value)
        self.write("Cookie has been set.<br>")

        # Verify and read back the cookie
        signed_value = self.get_cookie("mycookie")
        cookie_value = verify_signed_value(SECRET_KEY, 'cookie_name', signed_value)
        if cookie_value:
            self.write(f"Cookie value: {cookie_value}")
        else:
            self.write("Invalid cookie!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Starting Tornado server on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
