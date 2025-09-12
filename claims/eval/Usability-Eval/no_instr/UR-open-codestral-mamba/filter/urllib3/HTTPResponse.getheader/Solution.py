import urllib3

http = urllib3.PoolManager()

def get_header(url):
    response = http.request('GET', url)
    return response.headers

# To get the headers for a specific url
url = 'http://example.com'
headers = get_header(url)
print(headers)
