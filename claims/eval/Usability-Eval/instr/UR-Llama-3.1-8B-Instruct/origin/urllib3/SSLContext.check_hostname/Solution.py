import urllib3
from urllib3.util import ssl_
from urllib3.exceptions import GetattrError

def enable_hostname_matching():
    # Enable hostname matching using ProxyManager or PoolManager
    try:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        proxy_manager = urllib3.ProxyManager(
            num_pools=10,
            maxsize=10,
            cert_reqs='CERT_REQUIRED',
            ssl_version=ssl_.PROTOCOL_TLS_CLIENT,
            assert_hostname=True,
            verify_ssl=True,
            ssl_ca_certs='cacert.pem',
            timeout=5.0
        )
    except AttributeError:
        raise Exception("POOLS_REMOVE parameter is missed from Python35+")

    return proxy_manager

def enable_hostname_matching_pool_manager():
    # Enable hostname matching using PoolManager
    pool_manager = urllib3.PoolManager(
        num_pools=10,
        maxsize=10,
        cert_reqs='CERT_REQUIRED',
        ssl_version=ssl_.PROTOCOL_TLS_CLIENT,
        assert_hostname=True,
        timeout=5.0,
        ca_certs='cacert.pem'
    )

    return pool_manager

def test_hostname_matching(proxy_manager):
    try:
        # Send a HTTPS request using proxy
        r = proxy_manager.request(
            'GET',
            'https://www.google.com'
        )
        print(r.status)
    except (GetattrError,sslib_.SSLError, urllib3.exceptions.ProxyError) as e:
        print(e)

def test_hostname_matching_pool_manager(pool_manager):
    try:
        # Send a HTTPS request using pool manager
        r = pool_manager.request(
            'GET',
            'https://www.google.com'
        )
        print(r.status)
    except (GetattrError,sslib_.SSLError, urllib3.exceptions.ConnectionError) as e:
        print(e)

# Usage
if __name__ == "__main__":
    proxy_manager = enable_hostname_matching()
    test_hostname_matching(proxy_manager)

    pool_manager = enable_hostname_matching_pool_manager()
    test_hostname_matching_pool_manager(pool_manager)
