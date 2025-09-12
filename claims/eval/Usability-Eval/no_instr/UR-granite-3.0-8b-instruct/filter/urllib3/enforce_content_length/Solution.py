import urllib3

def check_content_length(response):
    content_length = response.headers.get('Content-Length')
    if content_length is None:
        # If Content-Length header is not present, no need to check
        return

    try:
        content_length = int(content_length)
    except ValueError:
        # If Content-Length header value is not an integer, raise error
        raise ValueError("Content-Length header value must be an integer")

    if len(response.data) != content_length:
        # If body length does not match Content-Length header, raise error
        raise ValueError("Body length does not match Content-Length header")

# Example usage:
http = urllib3.PoolManager()
response = http.request('GET', 'http://example.com')
check_content_length(response)
