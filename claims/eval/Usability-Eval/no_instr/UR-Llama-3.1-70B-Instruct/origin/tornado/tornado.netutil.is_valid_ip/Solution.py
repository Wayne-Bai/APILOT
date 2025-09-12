import tornado.ioloop
import tornado.web
import ipaddress

class IpAddressHandler(tornado.web.RequestHandler):
    def get(self):
        ip = self.get_argument('ip')
        try:
            ipaddress.ip_address(ip)
            self.write('True')
        except ValueError:
            self.write('False')

def make_app():
    return tornado.web.Application([
        (r'/isvalid', IpAddressHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
