import urllib3
from urllib3 import make_headers
from urllib3.exceptions import HTTPError

def send_chunked_request(url, headers=None):
    http = urllib3.PoolManager()
    # Chunked transfer encoding header
    if headers is None:
        headers = {}
    headers.update(make_headers(transfer_encoding='chunked'))

    def data_stream():
        yield b"chunk 1"
        yield b"chunk 2"
        yield b"chunk 3"

    try:
        response = http.request(
            'POST',
            url,
            headers=headers,
            body=data_stream(),
            preload_content=False
        )
        
        # Ensure complete response is read
        with response:
            return response.status, response.data
    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url = 'http://httpbin.org/post'
status, data = send_chunked_request(url)

print(f"Response status: {status}")
print(f"Response data: {data.decode('utf-8')}")
