import urllib3

def connect_to_server(hostname, port=None):
    if hostname is None:
        raise ValueError("Hostname is not provided")

    if port is None:
        http = urllib3.PoolManager()
        http.connect(hostname)
    else:
        http = urllib3.PoolManager()
        http.connect((hostname, port))

    return http
