import urllib3

http = urllib3.PoolManager()

def read_response(url, amt=1024):
    response = http.request(f'GET {url}', headers={'User-Agent': 'Mozilla/5.0'})
    return response.data[:amt]
