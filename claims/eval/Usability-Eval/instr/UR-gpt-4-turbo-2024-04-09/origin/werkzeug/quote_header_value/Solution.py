from werkzeug.http import dump_header

def quote_header_value(value):
    return dump_header(value)

# Example usage
header_value = quote_header_value('hello world "example"')
print(header_value)
