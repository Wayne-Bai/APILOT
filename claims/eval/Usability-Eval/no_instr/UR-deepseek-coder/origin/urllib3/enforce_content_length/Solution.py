import urllib3

def enforce_content_length_checking(response):
    content_length_header = response.headers.get('Content-Length')
    if content_length_header:
        expected_length = int(content_length_header)
        actual_length = len(response.data)
        if expected_length != actual_length:
            raise ValueError(f"Content-Length mismatch: expected {expected_length}, got {actual_length}")

# Example usage
http = urllib3.PoolManager()

try:
    response = http.request('GET', 'http://example.com')
    enforce_content_length_checking(response)
    print("Content-Length matches the expected length.")
except ValueError as e:
    print(e)
