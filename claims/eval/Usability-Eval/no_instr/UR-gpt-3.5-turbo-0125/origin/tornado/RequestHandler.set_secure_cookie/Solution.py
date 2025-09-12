
import tornado.web
from tornado.escape import json_encode

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_secure_cookie("cookie_name", "cookie_value")
        self.write("Cookie has been signed and timestamped.")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], cookie_secret="my_secret_key")

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
