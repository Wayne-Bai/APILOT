import tornado.web
import tornado.escape
import time
import hmac
import hashlib
import base64

class BaseHandler(tornado.web.RequestHandler):
    def get_secure_cookie(self, name):
        """Returns the given signed cookie if it validates, or None."""
        value = self.get_cookie(name)
        if value is None:
            return None

        signature = self.get_cookie(name + '_signature')
        if signature is None:
            return None

        # Create a new hash object and update it with the secret key and name of cookie
        hash_object = hmac.new(self.application.settings["cookie_secret"], 
                               name + value, 
                               hashlib.sha256).digest()

        # Get the signature from hash object and decode it from base64 encoding
        expected_signature = base64.b64encode(hash_object)

        # If the signature from cookie is the same as the expected signature
        if signature == expected_signature:
            return value
        else:
            return None


if __name__ == "__main__":
    settings = {
        "cookie_secret": "your secret key here",
    }
    app = tornado.web.Application([
        (r"/", BaseHandler),
    ], **settings)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
