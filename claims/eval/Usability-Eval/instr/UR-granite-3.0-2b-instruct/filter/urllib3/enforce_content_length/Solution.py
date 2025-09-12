import urllib3

http = urllib3.PoolManager()

def check_content_length(url):
    response = http.request(
        'GET', url,
        headers={'User-Agent': 'Mozilla/5.0'},
        timeout=10
    )

    if response.status != 200:
        raise Exception(f'Request failed with status code {response.status}')

    content_length = int(response.headers.get('Content-Length', 0))
    received_data = response.data

    if len(received_data) != content_length:
        raise Exception(f'Content length does not match. Received {len(received_data)}, expected {content_length}')

# Usage
check_content_length('https://example.com')
