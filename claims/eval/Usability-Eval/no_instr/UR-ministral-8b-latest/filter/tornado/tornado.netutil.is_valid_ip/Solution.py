import tornado.ioloop
import tornado.web
import re

class IPAddressCheckerHandler(tornado.web.RequestHandler):
    def get(self):
        query = self.get_query_argument("ip")
        if self.is_valid_ip(query):
            self.write("True")
        else:
            self.write("False")

    def is_valid_ip(self, ip):
        # IPv4 Regex
        ipv4_pattern = re.compile(r'^(\d+(\.\d+){3})\Z')
        # Check if the IP matches IPV4 pattern
        return bool(ipv4_pattern.match(ip))

application = tornado.web.Application([
    (r"/check_ip", IPAddressCheckerHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    print("Server running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
