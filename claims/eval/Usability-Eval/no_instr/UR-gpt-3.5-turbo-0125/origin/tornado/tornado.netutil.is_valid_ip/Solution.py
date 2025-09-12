
import tornado.ioloop
import tornado.web

class IPValidationHandler(tornado.web.RequestHandler):
    def get(self):
        ip_address = self.get_argument("ip_address")
        is_valid = self.validate_ip(ip_address)
        self.write(str(is_valid))

    def validate_ip(self, ip):
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit():
                return False
            num = int(part)
            if num < 0 or num > 255:
                return False
        return True

def make_app():
    return tornado.web.Application([
        (r"/validate_ip", IPValidationHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
