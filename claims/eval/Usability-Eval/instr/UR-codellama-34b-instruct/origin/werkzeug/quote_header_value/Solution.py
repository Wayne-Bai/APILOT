from werkzeug.wrappers import Request
from werkzeug.datastructures import Headers

def quote_header(header_name):
    """Quote a header value if necessary."""
    request = Request.from_values(headers={'Content-Type': 'application/json; charset=utf-8'})
    headers = request.headers
    header_value = headers[header_name]
    quoted_header_value = Headers._quote_header_value(header_value)
    return quoted_header_value
