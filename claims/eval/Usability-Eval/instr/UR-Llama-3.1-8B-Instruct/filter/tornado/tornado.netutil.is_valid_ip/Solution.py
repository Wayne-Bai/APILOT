import re

def validate_ip(ip):
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(pattern, ip))

import tornado.ioloop
import tornado.web

class IPValidationHandler(tornado.web.RequestHandler):
    def get(self):
        ip = self.get_argument("ip", "")
        if validate_ip(ip):
            self.write("True")
        else:
            self.write("False")

def make_app():
    return tornado.web.Application([
        (r"/validate-ip", IPValidationHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
