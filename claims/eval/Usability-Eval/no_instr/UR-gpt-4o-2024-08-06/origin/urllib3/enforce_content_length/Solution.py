import urllib3
from urllib3.exceptions import HTTPError

def fetch_with_content_length_check(url):
    http = urllib3.PoolManager()

    try:
        response = http.request('GET', url, preload_content=False)
        content_length_header = response.headers.get('Content-Length')

        if content_length_header:
            content_length = int(content_length_header)
            body = response.read()

            actual_length = len(body)
            if actual_length != content_length:
                raise ValueError(f"Content length mismatch: Expected {content_length} but got {actual_length}")

            return body

        else:
            return response.read()

    except HTTPError as e:
        print(f"HTTP error occurred: {e}")
    finally:
        response.release_conn()

# Example usage
url = 'http://example.com'
try:
    content = fetch_with_content_length_check(url)
    print("Content fetched successfully")
except ValueError as ve:
    print(ve)
