from werkzeug import unquote_header_value

header_value = 'Example "Header"'
unquoted_value = unquote_header_value(header_value)

print(unquoted_value)
