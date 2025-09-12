# Import necessary modules
from mitmproxy import ctx, http

# Define a class for the mitmproxy addon
class HeaderValidator:
    def __init__(self):
        self.invalid_requests = 0

    def http_connect(self, flow):
        self.validate_headers(flow.request)

    def http_request(self, flow):
        self.validate_headers(flow.request)

    def validate_headers(self, request):
        content_length = request.headers.get("content-length", "0")
        transfer_encoding = request.headers.get("transfer-encoding")

        if content_length!= "0" and transfer_encoding == "chunked":
            ctx.log.warn("Request smuggling attack detected!")
            self.invalid_requests += 1
            ctx.master.shutdown()

        if transfer_encoding == "chunked":
            cl = 0
            te = []
            for line in request.text.splitlines():
                if line.startswith("chunk"):
                    chunk_size = int(line.split()[0], 16)
                    if chunk_size > 0:
                        content_length_str = request.headers.get("content-length")
                        if content_length_str is not None and content_length_str.isdigit():
                            cl = int(content_length_str)
                            if cl!= chunk_size:
                                ctx.log.warn("Request smuggling attack detected!")
                                self.invalid_requests += 1
                                ctx.master.shutdown()
                        te.append(chunk_size)
            if sum(te)!= cl:
                ctx.log.warn("Request smuggling attack detected!")
                self.invalid_requests += 1
                ctx.master.shutdown()

addons = [HeaderValidator()]
