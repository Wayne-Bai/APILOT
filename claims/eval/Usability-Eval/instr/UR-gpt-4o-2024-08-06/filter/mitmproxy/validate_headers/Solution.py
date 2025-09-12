from mitmproxy import http

class RequestHeaderValidator:
    def request(self, flow: http.HTTPFlow) -> None:
        # Validate headers to avoid request smuggling attacks
        try:
            self.validate_headers(flow.request.headers)
        except ValueError as e:
            flow.response = http.Response.make(
                400,  # 400 Bad Request
                f"Malformed headers: {str(e)}",
                {"Content-Type": "text/plain"}
            )

    def validate_headers(self, headers):
        # Simple validation logic to detect malformed headers
        for header, value in headers.items():
            if not self.is_valid_header_name(header) or not self.is_valid_header_value(value):
                raise ValueError(f'Invalid header: {header}: {value}')

    def is_valid_header_name(self, name):
        # Example validation for header name
        return bool(name and all(c.isalnum() or c in '-_' for c in name))

    def is_valid_header_value(self, value):
        # Example validation for header value
        return bool(value and '\n' not in value and '\r' not in value)

addons = [
    RequestHeaderValidator()
]
