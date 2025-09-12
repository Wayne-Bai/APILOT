import urllib3

def read_url(url, amt):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return response.data[:amt]
