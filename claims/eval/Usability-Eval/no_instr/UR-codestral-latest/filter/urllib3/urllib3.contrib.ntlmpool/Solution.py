import urllib3
from urllib3 import HTTPConnectionPool
from urllib3.util import make_headers

def ntlm_authenticated_request(url, username, password):
    # Disable SSL certificate warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Create a pool manager as it automatically manages connections pooling for your applications
    pool = HTTPConnectionPool(host='your_host', port=80)

    # Prepare the headers for the upcoming request
    headers = make_headers(basic_auth='{0}:{1}'.format(username, password))

    # Make a GET request to the specified URL and return the response
    response = pool.request('GET', url, headers=headers)
    return response
