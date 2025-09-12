import tornado.web
import tornado.ioloop
import tornado.escape
import hashlib
import time

class SecureCookieHandler(tornado.web.RequestHandler):
    def get(self):
        # Set a cookie with a secure timestamp
        self.set_secure_cookie("cookie_name", self.create_signed_cookie("cookie_value"))
        self.write("Cookie has been set.")

    def create_signed_cookie(self, value, timestamp=None):
        if timestamp is None:
            timestamp = int(time.time())
        # Create a signature using SHA256
        secret_key = "your_secret_key"
        signature = hashlib.sha256(f"{value}:{timestamp}:{secret_key}".encode()).hexdigest()
        return f"{value}:{timestamp}:{signature}"

    def check_signed_cookie(self, cookie_value):
        parts = cookie_value.split(":")
        if len(parts) != 3:
            return False
        value, timestamp, signature = parts
        secret_key = "your_secret_key"
        # Recreate the signature to verify
        valid_signature = hashlib.sha256(f"{value}:{timestamp}:{secret_key}".encode()).hexdigest()
        return valid_signature == signature

    def post(self):
        # Check the secure cookie when needed
        cookie_value = self.get_secure_cookie("cookie_name")
        if cookie_value:
            if self.check_signed_cookie(cookie_value.decode()):
                self.write("Valid cookie.")
            else:
                self.write("Invalid cookie.")
        else:
            self.write("No cookie found.")

def make_app():
    return tornado.web.Application([
        (r"/", SecureCookieHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
