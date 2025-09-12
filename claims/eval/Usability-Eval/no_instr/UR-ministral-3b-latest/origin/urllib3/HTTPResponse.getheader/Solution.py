import urllib3

http = urllib3.PoolManager()

def get_headers(url):
    try:
        response = http.request('GET', url)
        headers = response.headers
        return headers.get('x-test-header')
    except Exception as e:
        return str(e)
