from werkzeug.wrappers import Request

def dump_http_header(header_name):
    # Create a request object
    request = Request('http://example.com')

    # Get the HTTP header value
    header_value = request.headers.get(header_name)

    # Print the HTTP header value
    print(f"{header_name}: {header_value}")

# Call the function with the desired header name
dump_http_header('User-Agent')
