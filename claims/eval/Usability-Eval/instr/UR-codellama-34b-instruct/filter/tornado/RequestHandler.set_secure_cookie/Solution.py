
import tornado.web
from tornado.escape import json_encode, json_decode
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

class CookieSigningHandler(tornado.web.RequestHandler):
    def get(self):
        # Generate a random nonce and add it to the cookie
        nonce = os.urandom(16)
        self.set_cookie("my_cookie", json_encode({"nonce": nonce}))

        # Sign the cookie using the SecureCookie class
        signed_cookie = tornado.web.SecureCookie(self, "my_cookie")
        signed_cookie["value"] = self.get_argument("value")
        signed_cookie["expires"] = self.get_argument("expires")
        signed_cookie["nonce"] = nonce
        self.set_cookie("my_cookie", signed_cookie)

    def post(self):
        # Verify the cookie using the SecureCookie class
        verified_cookie = tornado.web.SecureCookie(self, "my_cookie")
        if verified_cookie["value"] != self.get_argument("value"):
            raise HTTPError(403)
        elif verified_cookie["expires"] < datetime.utcnow():
            raise HTTPError(410)
        else:
            return verified_cookie
