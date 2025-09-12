import urllib3

def get_request(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return response
