from mitmproxy import http

class RequestValidator:
    def __init__(self, proc):
        self.proc = proc

    def request(self, flow: http.HTTPFlow) -> None:
        # Your validation logic here
        try:
            self.validate_headers(flow.request.headers)
        except ValueError as e:
            raise e

    def validate_headers(self, headers):
        # Example validation: Should start with a printable ASCII character
        for key, value in headers.items():
            if not key.isprintable() or not value.isprintable():
                raise ValueError("Malformed header key or value")
