import re
import tornado.ioloop
import tornado.web

class IPAddressChecker(tornado.web.RequestHandler):
    def get(self):
        ip_address = self.get_argument('ip_address', None)
        pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
        if pattern.match(ip_address):
            self.write(b'True')
        else:
            self.write(b'False')

def make_app():
    return tornado.web.Application([
        (r'/check_ip', IPAddressChecker),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().run_until_complete(app)
