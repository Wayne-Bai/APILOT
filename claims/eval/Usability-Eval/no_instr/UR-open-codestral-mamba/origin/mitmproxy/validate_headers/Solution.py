import mitmproxy
from mitmproxy import ctx

class HeaderValidator:
    def request(self, flow):
        # Check if the request contains the host header
        if 'host' not in flow.request.headers:
            ctx.log.error("Malformed request: Missing host header")
            raise ValueError("Malformed request: Missing host header")

def start():
    ctx.log.info("Starting Header Validator")

def load(l):
    l.addons.add(HeaderValidator())
