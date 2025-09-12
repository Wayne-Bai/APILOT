import urllib3

def enforce_content_length_check(url):
    http = urllib3.PoolManager()

    res = http.request('GET', url)

    # Checks if Content-Length is present in the response header
    if 'Content-Length' in res.headers:
        content_length_header = int(res.headers['Content-Length'])
        data_length = len(res.data)

        if content_length_header != data_length:
            raise ValueError('Content-Length mismatch')

    return res.data
