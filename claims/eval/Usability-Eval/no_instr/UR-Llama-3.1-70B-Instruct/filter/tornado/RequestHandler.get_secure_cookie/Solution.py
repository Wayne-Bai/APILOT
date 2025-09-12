import tornado.web
import tornado.escape
import base64
import hmac
import hashlib

def get_secure_cookie_value(cookie_name, value):
    """
    Returns the given signed cookie if it validates, or None.
    """
    if value is None:
        return None

    parts = value.split('!')
    if len(parts)!= 3:
        return None

    signature = hmac.new(tornado.options.options.cookie_secret, parts[0] + '!' + parts[1], hashlib.sha1).hexdigest()
    if not tornado.escape.utf8(signature) == parts[2]:
        return None

    return base64.b64decode(tornado.escape.utf8(parts[1]))

class BaseHandler(tornado.web.RequestHandler):
    def get_secure_cookie(self, name):
        value = self.get_cookie(name)
        if value is not None:
            return get_secure_cookie_value(name, value)
        else:
            return None

    def set_secure_cookie(self, name, value):
        """
        Sign the given cookie name with the given value and set it on the browser.
        """
        timestamp = tornado.escape.utf8(str(int(time.time())))
        value = base64.b64encode(tornado.escape.utf8(value))
        signature = hmac.new(tornado.options.options.cookie_secret, name + '!' + timestamp + '!' + value, hashlib.sha1).hexdigest()
        self.set_cookie(name, name + '!' + timestamp + '!' + value + '!' + signature)

# Usage
if __name__ == "__main__":
    import tornado.ioloop
    import tornado.options
    from tornado.options import define, options
    import time

    define("cookie_secret", "some_secret_key", type=str)

    tornado.options.parse_command_line()

    app = tornado.web.Application([
        (r"/", BaseHandler),
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
