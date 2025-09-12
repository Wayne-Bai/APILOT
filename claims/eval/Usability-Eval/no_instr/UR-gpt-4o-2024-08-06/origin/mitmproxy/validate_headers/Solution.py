from mitmproxy import http

class ValidateHeaders:
    def validate_headers(self, headers):
        for header in headers.items():
            if not self.is_header_valid(header):
                raise ValueError(f"Malformed header detected: {header}")

    def is_header_valid(self, header):
        # Example validation logic: Check if the header name and value have basic valid characteristics
        name, value = header
        if not name or not isinstance(name, str) or len(name) > 256:
            return False
        if not value or not isinstance(value, str) or len(value) > 4096:
            return False
        # Add more validation rules as needed
        return True

    def request(self, flow: http.HTTPFlow) -> None:
        try:
            # Validate request headers
            self.validate_headers(flow.request.headers)
        except ValueError as ve:
            flow.response = http.Response.make(
                400,  # Bad request
                b"Invalid headers",
                {"Content-Type": "text/plain"}
            )
            flow.error = str(ve)

addons = [
    ValidateHeaders()
]
