import urllib3

def connection_manager(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return response.data
