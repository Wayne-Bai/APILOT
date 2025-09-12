import urllib3

def check_sni(pool, host, port):
    if not pool.get_address(host, port):
        print("Warning: No SNI available for {}".format(host))
        return False
    return True

http = urllib3.PoolManager()

def make_request(host, port, method, **kwargs):
    if not check_sni(http.pool, host, port):
        raise ValueError("No SNI available for {}:{}".format(host, port))

    url = "https://{}:{}".format(host, port)
    response = http.request(method, url, **kwargs)
    return response

# Usage
make_request("example.com", 443, "GET", headers={"User-Agent": "MyApp/1.0"})
