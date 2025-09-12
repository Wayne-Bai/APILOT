import urllib3

def enforce_content_length(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)

    content_length = r.headers.get('content-length')
    if content_length and len(r.data) != int(content_length):
        raise ValueError("Body returned by server does not match value of Content-Length header.")

    return r.data
