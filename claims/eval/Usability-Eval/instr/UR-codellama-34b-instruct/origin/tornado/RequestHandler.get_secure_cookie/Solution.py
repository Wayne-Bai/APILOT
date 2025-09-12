import hmac
import hashlib
from tornado.web import RequestHandler

class SecureCookieHandler(RequestHandler):
    def get_secure_cookie(self, name):
        cookie = self.request.cookies[name]
        if not cookie:
            return None
        # Check if the cookie has expired
        if cookie.expires < datetime.utcnow():
            return None
        # Check if the cookie signature is valid
        signature = cookie.signature
        expected_signature = hmac.new(self._get_secret_key(), msg=cookie.value, digestmod=hashlib.sha256).digest()
        if not hmac.compare_digest(signature, expected_signature):
            return None
        # Return the cookie value if it's valid
        return cookie.value
