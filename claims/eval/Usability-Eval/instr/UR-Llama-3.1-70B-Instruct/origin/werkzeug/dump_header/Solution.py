from werkzeug import http
from werkzeug.datastructures import Headers

def dump_header(header):
    """
    Dump an HTTP header.

    :param header: The HTTP header to dump.
    """
    # Ensuring the header is a Headers object
    if not isinstance(header, Headers):
        header = Headers(header)

    # Dumping the header
    dumped_header = ""
    for key, value in header:
        dumped_header += f"{key}: {value}\n"

    return dumped_header

# Example usage
header = [
    ("Content-Type", "application/json"),
    ("Content-Length", "12345"),
    ("Set-Cookie", "session=abc123")
]

dumped_header = dump_header(header)
print(dumped_header)
