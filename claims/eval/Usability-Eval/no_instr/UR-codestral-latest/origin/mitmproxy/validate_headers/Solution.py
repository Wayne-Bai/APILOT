from mitmproxy import ctx
import re

def request(flow):
    headers = flow.request.headers

    for name, value in headers.items():
        # Check if header name or values contains invalid characters
        if not re.fullmatch(r'[^\s\:]{1,}', name):
            raise ValueError(f"Malformed header name: {name}")
        if not re.fullmatch(r'[^\x00-\x1F\x7F]{1,}', value):
            raise ValueError(f"Malformed header value: {value}")
