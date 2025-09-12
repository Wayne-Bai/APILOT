import tornado.web
import ipaddress

def is_valid_ip(ip_str):
    try:
        ipaddress.IPv4Address(ip_str)
        return True
    except ValueError:
        return False

class IPAddressHandler(tornado.web.RequestHandler):
    def get(self):
        ip_address = self.get_argument('ip')
        is_valid = is_valid_ip(ip_address)
        self.write(is_valid)
