import urllib.request

def get_headers(url):
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            return response.info()
    except Exception as e:
        return str(e)

url = "http://example.com"
print(get_headers(url))
