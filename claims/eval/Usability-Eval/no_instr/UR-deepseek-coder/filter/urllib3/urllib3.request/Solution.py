import urllib3

def request(method, url, fields=None, headers=None, **urlopen_kw):
    # Create a new PoolManager instance to avoid side effects
    http = urllib3.PoolManager()
    
    # Perform the request using the PoolManager instance
    response = http.request(method, url, fields=fields, headers=headers, **urlopen_kw)
    
    return response
