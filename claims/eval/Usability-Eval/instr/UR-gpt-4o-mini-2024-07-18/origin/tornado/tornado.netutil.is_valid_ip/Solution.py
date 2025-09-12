import tornado.ioloop
import tornado.web
import re

def is_valid_ip(ip):
    # Regular expression to validate an IPv4 address
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ip):
        octets = ip.split('.')
        return all(0 <= int(octet) <= 255 for octet in octets)
    return False

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        ip = self.get_query_argument("ip", None)
        if ip and is_valid_ip(ip):
            self.write({"valid": True})
        else:
            self.write({"valid": False})

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
