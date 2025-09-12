import tornado.web
import base64
import hmac
import time
import hashlib

class BaseHandler(tornado.web.RequestHandler):
    def set_secure_cookie(self, name, value, expires_days=30, version=None, **kwargs):
        secret = "your_secret_key"
        timeout = time.time() + expires_days * 86400
        value = "%s|%s" % (base64.b64encode(value), int(timeout))
        signature = self._get_signature(secret, value)
        value = "%s|%s" % (value, signature)
        self.set_cookie(name, value, path="/", expires=timeout, **kwargs)

    def _get_signature(self, secret, value):
        return hmac.new(secret, value, hashlib.sha1).hexdigest()

    def get_secure_cookie(self, name, value=None, max_age_days=31, min_version=None):
        # To get the secure cookie and check its validity
        pass
