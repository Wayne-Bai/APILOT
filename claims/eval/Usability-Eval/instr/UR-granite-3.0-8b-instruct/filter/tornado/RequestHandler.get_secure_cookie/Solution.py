import tornado.web
from tornado.escape import json_encode
from tornado.options import define, options
from tornado.auth import TwitterAuthOAuth, OAuthOptions
from tornado.httpauth import OAuthAuth, BasicAuth
from tornado.auth import AuthMiddleware
from tornado.escape import to_base64
import base64
import hashlib
import time

define("oauth_consumer_key", default="", help="Twitter OAuth consumer key")
define("oauth_consumer_secret", default="", help="Twitter OAuth consumer secret")

class SignedCookieHandler(tornado.web.RequestHandler):
    def get(self):
        # Get the signed cookie from the request
        signed_cookie = self.get_secure_cookie("signed_cookie")

        # Validate the signed cookie
        if signed_cookie is None:
            return

        # Decode the signed cookie
        decoded_cookie = base64.b64decode(signed_cookie).decode("utf-8")

        # Split the decoded cookie into timestamp and signature
        timestamp, signature = decoded_cookie.split(".")

        # Calculate the expected signature
        expected_signature = hashlib.sha256((timestamp + options.oauth_consumer_secret).encode("utf-8")).hexdigest()

        # Validate the signature
        if not hmac.compare_digest(signature, expected_signature):
            return

        # If the signature is valid, return the signed cookie
        self.set_secure_cookie("signed_cookie", signed_cookie)
        self.write(signed_cookie)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/", SignedCookieHandler),
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
