import ipaddress
import tornado.web

class IPHandler(tornado.web.RequestHandler):
    def post(self):
        data = self.get_body_argument('data')
        try:
            ipaddress.ip_address(data)
            return self.write({'result': True})
        except ValueError:
            return self.write({'result': False})

def make_app():
    return tornado.web.Application([
        (r'/check_ip', IPHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
