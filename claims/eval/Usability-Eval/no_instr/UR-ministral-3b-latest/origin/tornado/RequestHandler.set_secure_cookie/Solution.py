import tornado.ioloop
import tornado.web
import time
import hashlib
import base64

class CookieHandler(tornado.web.RequestHandler):
    def get_cookie(self, key):
        value = self.get_cookie(key)
        if not value:
            return None
        return self._validate_signature(key, value)

    def set_cookie(self, key, value, sessionid=None):
        sig = self._hash(key, value)
        signed_value = base64.b64encode(sig.encode()).decode()
        self.set_cookie(key, value + '_' + signed_value, httponly=True)

    def _validate_signature(self, key, value):
        raw_value, sig = value.split('_')
        my_sig = self._hash(key, raw_value)
        valid = base64.b64decode(my_sig.encode()).decode() == sig
        if valid:
            self.set_cookie(f"{key}_validate", "true", overwrite=True)  # Let's store a secret (never send over a public channel)
        return valid

    def _hash(self, key, value):
        now = time.time()
        return hashlib.sha256((key + str(now)).encode() + value.encode()).digest()

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/set_cookie", CookieHandler),
        (r"/get_cookie", CookieHandler),
    ])
    app.listen(8888)
    print("Server is running at http://localhost:8888/")
    tornado.ioloop.IOLoop.current().start()
