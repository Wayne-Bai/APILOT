import urllib3

def read_response(url, amt=1024):
    http = urllib3.PoolManager()
    response = http.request('GET', url, preload_content=True)
    data = response.data
    return data[:amt]
