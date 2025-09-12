import tornado.web

class IPAddressHandler(tornado.web.RequestHandler):
    def get(self):
        ip_address = self.get_argument('ip_address')
        is_valid = self.is_valid_ip(ip_address)
        self.write({'is_valid': is_valid})

    def is_valid_ip(self, ip_address):
        parts = ip_address.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255:
                return False
        return True
