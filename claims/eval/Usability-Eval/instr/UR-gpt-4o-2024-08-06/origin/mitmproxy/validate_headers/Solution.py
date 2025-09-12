from mitmproxy import http
from mitmproxy import ctx

class HeaderValidator:
    def __init__(self):
        self.logger = ctx.log

    def request(self, flow: http.HTTPFlow) -> None:
        headers = flow.request.headers
        try:
            self.validate_headers(headers)
        except ValueError as e:
            flow.response = http.Response.make(
                400,  # Bad Request
                str(e),
                {"Content-Type": "text/plain"}
            )

    def validate_headers(self, headers) -> None:
        # A simple validation to ensure no duplicate headers
        seen = {}
        for header in headers:
            if header in seen:
                raise ValueError(f"Duplicate header found: {header}")
            seen[header] = True

        # Check for common problematic headers that can lead to smuggling
        if 'Transfer-Encoding' in headers:
            if 'Content-Length' in headers:
                raise ValueError("Both Transfer-Encoding and Content-Length headers found.")

        self.logger.info("Headers validated successfully.")

addons = [
    HeaderValidator()
]
