from mitmproxy import http
import mitmproxy

class HeaderValidator:
    def __init__(self):
        self.disallowed_headers = ["Transfer-Encoding", "Content-Length"]

    def validate_headers(self, flow: mitmproxy.http.HTTPFlow):
        for header in flow.request.headers.items():
            if header[0] in self.disallowed_headers:
                if len(header[1].split(',')) > 1:
                    raise ValueError("Malformed headers detected")

addons = [
    HeaderValidator()
]

def load(l):
    l.addon(HeaderValidator())
