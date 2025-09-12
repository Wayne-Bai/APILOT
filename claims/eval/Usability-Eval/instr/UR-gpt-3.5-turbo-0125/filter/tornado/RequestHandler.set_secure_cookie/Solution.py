
import tornado.web
import hashlib
import time

class MainHandler(tornado.web.RequestHandler):
    def get_signed_cookie(self, name, value):
        # Cookie value with timestamp
        timestamp = str(int(time.time()))
        hashed_value = hashlib.sha256(value.encode('utf-8') + timestamp.encode('utf-8')).hexdigest()
        self.set_secure_cookie(name, value + "|" + timestamp + "|" + hashed_value)

    def get(self):
        # Set signed cookie
        self.get_signed_cookie("my_cookie", "example_value")
        self.write("Cookie signed successfully")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
