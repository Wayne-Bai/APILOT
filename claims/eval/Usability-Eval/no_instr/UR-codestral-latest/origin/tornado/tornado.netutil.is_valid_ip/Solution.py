import tornado.ioloop
import tornado.web
import ipaddress

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        ip = self.get_argument('ip')
        try:
            ipaddress.ip_address(ip)
            self.write({'valid_ip': True})
        except ValueError:
            self.write({'valid_ip': False})

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
