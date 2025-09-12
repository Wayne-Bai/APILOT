import re
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

class IPAddressHandler(RequestHandler):
    def get(self):
        ip_address = self.get_argument('ip', None)
        if ip_address is None:
            self.write("IP address not provided.")
        else:
            if self.is_well_formed_ip(ip_address):
                self.write(f"The IP address {ip_address} is well-formed.")
            else:
                self.write(f"The IP address {ip_address} is not well-formed.")

    def is_well_formed_ip(self, ip):
        # Basic regex to validate an IPv4 address
        pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
        
        if pattern.match(ip):
            parts = ip.split('.')
            for part in parts:
                if int(part) < 0 or int(part) > 255:
                    return False
            return True
        return False

def make_app():
    return Application([
        (r"/check-ip", IPAddressHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server is running on http://localhost:8888")
    IOLoop.current().start()
