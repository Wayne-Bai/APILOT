
from werkzeug.wrappers import Request, Response
from werkzeug.utils import parse_qsl

def quote_header_value(value):
    return parse_qsl(value)

request = Request()
response = Response()

# Set the header value to be quoted
request.headers['Example-Header'] = 'Some header value'

# Quote the header value and add it to the response
response.headers['Quoted-Value'] = quote_header_value(request.headers['Example-Header'])
