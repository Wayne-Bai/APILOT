import tornado.web
import hashlib
import hmac
import time

class SecureCookieHandler(tornado.web.RequestHandler):
    def get(self):
        cookie_name = "my_secure_cookie"
        cookie_value = "some_value"
        secret_key = "your_secret_key"

        # Create a timestamp
        timestamp = str(int(time.time()))

        # Create the cookie value with the timestamp
        cookie_with_timestamp = f"{cookie_value}|{timestamp}"

        # Sign the cookie value
        signature = hmac.new(secret_key.encode(), cookie_with_timestamp.encode(), hashlib.sha256).hexdigest()

        # Combine the signed cookie value with the signature
        signed_cookie = f"{cookie_with_timestamp}|{signature}"

        # Set the secure cookie
        self.set_cookie(cookie_name, signed_cookie)

        self.write("Secure cookie set!")

    def post(self):
        cookie_name = "my_secure_cookie"
        secret_key = "your_secret_key"

        # Get the signed cookie from the request
        signed_cookie = self.get_cookie(cookie_name)

        if not signed_cookie:
            self.write("No secure cookie found!")
            return

        # Split the signed cookie into its components
        try:
            cookie_value, timestamp, received_signature = signed_cookie.split("|")
        except ValueError:
            self.write("Invalid cookie format!")
            return

        # Recreate the cookie value with the timestamp
        cookie_with_timestamp = f"{cookie_value}|{timestamp}"

        # Verify the signature
        expected_signature = hmac.new(secret_key.encode(), cookie_with_timestamp.encode(), hashlib.sha256).hexdigest()

        if not hmac.compare_digest(expected_signature, received_signature):
            self.write("Invalid cookie signature!")
            return

        # Verify the timestamp (e.g., check if it's within a reasonable time window)
        current_time = int(time.time())
        cookie_time = int(timestamp)

        if current_time - cookie_time > 3600:  # 1 hour window
            self.write("Cookie has expired!")
            return

        self.write(f"Secure cookie verified! Value: {cookie_value}")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/secure_cookie", SecureCookieHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
