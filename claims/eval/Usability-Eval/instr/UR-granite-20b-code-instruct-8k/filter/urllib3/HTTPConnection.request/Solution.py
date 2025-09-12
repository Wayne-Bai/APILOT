import urllib3

def send_request(method, url):
    http = urllib3.PoolManager()
    response = http.request(method, url)
    return response.data
