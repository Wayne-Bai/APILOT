import tornado.ioloop
import tornado.web
import re

class IPAddressHandler(tornado.web.RequestHandler):
    def get(self):
        ip_address = self.get_argument('ip', None)
        if ip_address and self.is_valid_ip(ip_address):
            self.write({'valid': True})
        else:
            self.write({'valid': False})

    def is_valid_ip(self, ip):
        # Regular expression to validate an IP address
        pattern = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
        if pattern.match(ip):
            parts = ip.split('.')
            return all(0 <= int(part) <= 255 for part in parts)
        return False

def make_app():
    return tornado.web.Application([
        (r"/validate_ip", IPAddressHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
