import tornado.web
import socket

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        ip = self.get_argument("ip")
        self.write("This is a well-formed IP address: %s" % str(is_valid_ip(ip)))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
