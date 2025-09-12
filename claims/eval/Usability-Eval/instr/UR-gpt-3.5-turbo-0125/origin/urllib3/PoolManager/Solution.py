
import urllib3
from urllib3 import PoolManager
from urllib3.connectionpool import connection_from_url

redirect_codes = [301, 302, 303, 307, 308]

def custom_cross_host_redirect_logic(response):
    if response.status in redirect_codes:
        location = response.getheader('Location')
        if location.startswith('http'):
            return location
        else:
            return "/".join(response.request.url.split('/')[:-1]) + '/' + location
    else:
        return None

# Custom connection pool with redirect logic
class RedirectPoolManager(PoolManager):
    def urlopen(self, method, url, body=None, headers=None, retries=None, redirect=True, assert_same_host=True, timeout=urllib3.Timeout.DEFAULT_TIMEOUT, pool_timeout=None, release_conn=None, chunked=False, body_pos=None, **response_kw):
        response = super(RedirectPoolManager, self).urlopen(method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
        
        new_location = custom_cross_host_redirect_logic(response)
        if new_location is not None:
            return self.urlopen(method, new_location, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)

        return response

# Create a pool manager with custom redirect logic
http = RedirectPoolManager()

# Example HTTP request
http.request('GET', 'http://www.example.com/path-to-resource')
