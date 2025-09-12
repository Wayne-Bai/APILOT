import urllib.request

def read_url(url, amt=None):
    with urllib.request.urlopen(url) as response:
        if amt:
            return response.read(amt)
        else:
            return response.read()
