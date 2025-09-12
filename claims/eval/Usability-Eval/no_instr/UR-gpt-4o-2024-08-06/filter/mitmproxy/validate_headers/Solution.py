from mitmproxy import http
from mitmproxy import ctx

class ValidateHeaders:
    def request(self, flow: http.HTTPFlow) -> None:
        try:
            self.validate_headers(flow)
        except ValueError as e:
            flow.response = http.Response.make(
                400,  # Bad Request status code
                f"Malformed headers: {str(e)}"
            )

    def validate_headers(self, flow: http.HTTPFlow) -> None:
        headers = flow.request.headers

        # Example header checks
        if "Content-Length" in headers and "Transfer-Encoding" in headers:
            raise ValueError("Both Content-Length and Transfer-Encoding headers are set.")

        if "Host" not in headers:
            raise ValueError("Missing Host header.")

        # Add more header validation logic as needed

        ctx.log.info("Headers validated successfully.")

addons = [
    ValidateHeaders()
]
