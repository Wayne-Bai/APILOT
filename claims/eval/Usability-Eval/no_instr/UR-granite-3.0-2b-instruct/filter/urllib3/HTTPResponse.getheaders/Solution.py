from urllib.request import Request, urlopen
from urllib.error import URLError

def get_headers(url):
    headers = {}
    request = Request(url)
    try:
        response = urlopen(request)
        headers = response.getheader().split('\r\n')
    except URLError as e:
        print(f"URL is not reachable: {e.reason}")
    return headers
