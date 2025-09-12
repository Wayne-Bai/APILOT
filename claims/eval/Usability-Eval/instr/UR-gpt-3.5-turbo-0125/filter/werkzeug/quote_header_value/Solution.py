
from werkzeug.http import quote_header_value

# Example code to quote a header value
header_value = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjM0NTY3ODkwLCJleHBpcmVkX3N0YW5'
quoted_header_value = quote_header_value(header_value)

print(quoted_header_value)
