import tornado.ioloop
import tornado.web
import ipaddress

class IPAddressHandler(tornado.web.RequestHandler):
    def get(self):
        ip = self.get_argument('ip', '')
        try:
            ipaddress.ip_address(ip)
            self.write({'status': True,'message': f'{ip} is a valid IP address'})
        except ValueError:
            self.write({'status': False,'message': f'{ip} is not a valid IP address'})

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/is_valid_ip", IPAddressHandler),
        ]
        settings = dict(
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)

def main():
    app = Application()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
