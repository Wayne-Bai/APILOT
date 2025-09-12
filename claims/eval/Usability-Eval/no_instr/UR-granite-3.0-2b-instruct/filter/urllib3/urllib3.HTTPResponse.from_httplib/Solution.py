import urllib3

def convert_http_response(r):
    http = urllib3.PoolManager()
    response = http.request('GET', r.url, headers=r.headers, body=None, streams=True)
    return response
