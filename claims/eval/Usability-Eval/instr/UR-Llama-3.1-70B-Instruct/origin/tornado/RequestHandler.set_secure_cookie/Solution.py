import tornado.ioloop
import tornado.web
import tornado.escape
import base64
import hmac
import time
import hashlib

class BaseHandler(tornado.web.RequestHandler):
    def set_secure_cookie(self, name, value, expires_days=30):
        expires = str(int(time.time() + expires_days * 24 * 60 * 60))
        value = base64.b64encode(tornado.escape.utf8(value)).decode('utf-8')
        signature = self._cookie_signature(name, value, expires)
        self.set_cookie(name, unnatural_cookie_string(value, expires, signature))

    def _cookie_signature(self, name, value, expires):
        secret_key = self.application.settings.get('cookie_secret')
        string = '%s|%s|%s' % (name, value, expires)
        sig = hmac.new(secret_key, string.encode('utf-8'), hashlib.sha256).hexdigest()
        return sig

    def get_secure_cookie(self, name):
        value = unnatural_cookie_unstring(self.get_cookie(name))
        if not value:
            return None
        value, expires, signature = value
        if not self._check_signature(name, value, expires, signature):
            return None
        return value

    def _check_signature(self, name, value, expires, signature):
        secret_key = self.application.settings.get('cookie_secret')
        new_signature = self._cookie_signature(name, value, expires)
        return new_signature == signature

def unnatural_cookie_string(value, timestamp, signature):
    return '%s|%s|%s' % (value, timestamp, signature)

def unnatural_cookie_unstring(cookie):
    if not cookie:
        return ''
    parts = cookie.split('|')
    if len(parts)!= 3:
        return ''
    (value, timestamp, signature) = parts
    try:
        return (base64.b64decode(value).decode('utf-8'), int(timestamp), signature)
    except ValueError:
        return ''

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/set_cookie", BaseHandler),
        ]
        settings = {'cookie_secret': 'your_secret_key'}
        super(Application, self).__init__(handlers, **settings)

if __name__ == "__main__":
    app = Application()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
