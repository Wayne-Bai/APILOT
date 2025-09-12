from mitmproxy.models import HTTPRequest, HTTPResponse
from cytools import HTTP

class ValidateHeaders:
    def __init__(self):
        pass

    def request(self, flow:'mitmproxy.Flow') -> None:
        # Extract the request headers from the flow
        request_headers = flow.request.headers

        try:
            # Attempt to create an HTTP object using the request headers
            http = HTTP(request_headers.to_dict())
        except Exception as e:
            # If the request headers are malformed, raise a ValueError
            raise ValueError(f"Malformed request headers: {str(e)}")

        # Validate the request headers
        http.validate_request_headers()

def configure(m):
    m.addons.append(ValidateHeaders())

# Add this configuration to mitmproxy to validate every incoming request
