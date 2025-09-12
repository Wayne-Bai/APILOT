import urllib3

http = urllib3.PoolManager()

def top_level_request(method, url, **kwargs):
    response = http.request(method, url, **kwargs)
    return response
