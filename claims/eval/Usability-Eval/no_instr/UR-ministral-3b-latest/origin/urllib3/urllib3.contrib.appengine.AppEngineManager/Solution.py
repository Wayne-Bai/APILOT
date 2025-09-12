import urllib3

from urllib3.exceptions import InsecureRequestWarning

# Suppress Only If Required
urllib3.disable_warnings(InsecureRequestWarning)

# To specify a base pool manager with a retry policy
http = urllib3.PoolManager()
