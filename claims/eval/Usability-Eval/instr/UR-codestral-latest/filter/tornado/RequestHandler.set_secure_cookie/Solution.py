import tornado.ioloop
import tornado.web
import time
import hmac
import hashlib
import binascii

# secret key for signing
SECRET_KEY = b'your-secret-key'

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # sign the cookie value with the current timestamp
        value = str(int(time.time()))
        hasher = hmac.new(SECRET_KEY, value.encode(), hashlib.sha256)
        signed_value = value + ':' + binascii.hexlify(hasher.digest()).decode()

        # set the secure cookie
        self.set_secure_cookie("user", signed_value)

        self.write("Cookie set.")

    def post(self):
        # get the last cookie we set
        signed_value = self.get_secure_cookie("user").decode()

        # make sure the cookie value is correctly signed
        value, received_sig = signed_value.split(':')
        hasher = hmac.new(SECRET_KEY, value.encode(), hashlib.sha256)
        computed_sig = binascii.hexlify(hasher.digest()).decode()

        if computed_sig != received_sig:
            self.write("Invalid cookie.")
            return

        self.write("Cookie is valid.")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
