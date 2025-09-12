import mitmproxy
from mitmproxy.exceptions import ValueError

# Create a new mitmproxy instance
mitm = mitmproxy.MitmProxy()

# Define a function to validate HTTP headers
def validate_headers(headers):
    # Check if the headers are malformed
    if not mitm.is_valid_header_name(headers['Name']):
        raise ValueError("Malformed header name")
    elif not mitm.is_valid_header_value(headers['Value']):
        raise ValueError("Malformed header value")

# Add the function as a hook to validate headers
mitm.add_hook('on_request', validate_headers)
