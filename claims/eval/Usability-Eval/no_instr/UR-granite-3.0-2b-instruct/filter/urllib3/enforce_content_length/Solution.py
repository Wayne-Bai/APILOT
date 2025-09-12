import urllib3

http = urllib3.PoolManager()

def check_content_length(url):
    response = http.request('GET', url, headers={'Content-Length': '1234'})  # replace 1234 with the expected content length

    if response.status != 200:
        raise Exception(f"Request failed with status code {response.status}")

    if response.head.get('Content-Length') != '1234':
        raise Exception("Content length in response does not match the expected value")

# Usage
check_content_length('https://example.com')
