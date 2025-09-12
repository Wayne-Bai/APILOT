
from werkzeug.http import unquote_header_value
header_value = 'This%20is%20a%20header%20value'
unquoted_header = unquote_header_value(header_value)
print(unquoted_header)
