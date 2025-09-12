import tornado.ioloop
import tornado.web
import time
import hmac
import hashlib
import base64

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Generate a random key for signing and timestamping
        key = "my_secret_key"
        timestamp = int(time.time())

        # Create a message to be signed
        message = f"{timestamp}:{self.request.uri}".encode()

        # Create a signature using the key and the message
        signature = hmac.new(key.encode(), message, hashlib.sha256).digest()

        # Base64 encode the signature
        signed_message = base64.b64encode(signature).decode()

        # Create the cookie with the signed message and timestamp
        self.set_cookie("signed_cookie", f"{signed_message}:{timestamp}")

        # Return a response
        self.write("Cookie signed and timestamped")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().run_until_complete(app)
