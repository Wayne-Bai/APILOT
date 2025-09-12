import os
import base64
import datetime
import hmac
import hashlib
import tornado.ioloop
import tornado.web

SECRET_KEY = os.environ.get("SECRET_KEY")

def sign_cookie(cookie_value, secret_key):
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")
    value = base64.b64encode(cookie_value.encode()).decode() + "|" + timestamp
    signature = hmac.new(secret_key.encode(), value.encode(), hashlib.sha256).hexdigest()
    return f"{value}|{signature}"

def verify_cookie(cookie_value, secret_key):
    try:
        value, signature = cookie_value.rsplit("|", 1)
        expected_signature = hmac.new(secret_key.encode(), value.encode(), hashlib.sha256).hexdigest()
        return hmac.compare_digest(expected_signature, signature)
    except:
        return False

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cookie_value = self.get_argument("cookie_value")
        if verify_cookie(cookie_value, SECRET_KEY):
            self.write("Cookie is valid")
        else:
            self.write("Cookie is invalid")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
