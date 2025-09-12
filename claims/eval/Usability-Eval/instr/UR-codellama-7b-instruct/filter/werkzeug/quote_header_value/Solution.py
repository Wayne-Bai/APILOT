
from werkzeug.routing import request

# Get the value of the 'Authorization' header from the request
auth_header = request.headers['Authorization']

# Quote the 'Authorization' header value if necessary
if not auth_header.isascii():
    quoted_auth_header = auth_header.encode('utf-8').quote()
else:
    quoted_auth_header = auth_header

print(quoted_auth_header)
