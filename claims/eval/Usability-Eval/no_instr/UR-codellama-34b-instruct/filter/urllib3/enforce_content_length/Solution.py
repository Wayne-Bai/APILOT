import urllib3

def fetch_content(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    if 'Content-Length' in response.headers and int(response.headers['Content-Length']) != len(response.data):
        raise ValueError("Content length mismatch")
    return response.data
