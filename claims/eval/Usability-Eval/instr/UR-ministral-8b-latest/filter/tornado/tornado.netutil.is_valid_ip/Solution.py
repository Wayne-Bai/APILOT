import re
import tornado.ioloop
import tornado.web

def is_valid_ip(ip):
    # Check if the IP address contains a value between 0-255 in each octet
    pattern = re.compile(r"^(?:[0-9]{1,3}\.)(?:[0-9]{1,3}\.)(?:[0-9]{1,3}\.)(?:[0-9]{1,3})$")
    if not pattern.match(ip):
        return False
    octets = ip.split('.')
    for octet in octets:
        if not 0 <= int(octet) <= 255:
            return False
    return True

class ValidIPHandler(tornado.web.RequestHandler):
    def get(self):
        ip = self.get_argument('ip')
        if is_valid_ip(ip):
            self.write('True')
        else:
            self.write('False')

if __name__ == '__main__':
    application = tornado.web.Application([
        (r'/', ValidIPHandler)
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
