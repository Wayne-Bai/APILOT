import urllib3

def check_content_length(response):
    content_length = response.headers.get('Content-Length')
    if content_length:
        content_length = int(content_length)
        if content_length != len(response.data):
            raise ValueError("Content length mismatch")
    else:
        # If Content-Length header is not present, you can set a default value or raise an error as per your requirement
        pass

# Usage
http = urllib3.PoolManager()
response = http.request('GET', 'http://example.com')
check_content_length(response)
