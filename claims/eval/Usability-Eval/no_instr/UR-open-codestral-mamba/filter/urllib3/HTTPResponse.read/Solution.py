import urllib3

def get_response_body(url, amt=None):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    data = response.data[:amt] if amt else response.data
    return data
