
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from ssl.py about deprecated create_default_context
import urllib3
urllib3.disable_warnings(InsecureRequestWarning)

import ssl

# Create a HTTPS context
https_context = ssl.create_default_context()

# Set the CA certificate for the context, if desired
# https_context.check_hostname = False
# https_context.verify_mode = ssl.CERT_NONE

# You might need to use this line of code if you have a certificate
# or pair of certificates somewhere on your computer
# https_context.load_verify_locations("/path/to/cert/cacert.pem")

#Create a helper function to connect to https server using computed https context
def connect_to_https_server(url, timeout=10, cert_reqs=ssl.CERT_NONE):
    connection_pool = urllib3.PoolManager(
        cert_reqs=cert_reqs,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'},
        tls=https_context,
        timeout=timeout
    )

    try:
        # Attempt to create a transport and request
        response = connection_pool.request('GET', url)
        
        print(response.status, response.data)

    except Exception as ex:
        print(f"An error occurred: {ex}")
