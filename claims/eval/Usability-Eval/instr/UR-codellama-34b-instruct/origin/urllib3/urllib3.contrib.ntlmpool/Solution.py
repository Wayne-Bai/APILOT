import requests
from urllib3 import PoolManager
from ntlm_auth.ntlm import NtlmAuthentication

# Set up the NTLM authentication object
auth = NtlmAuthentication()

# Set up the URL and parameters for the API call
url = "https://example.com/api/endpoint"
params = {
    "param1": "value1",
    "param2": "value2"
}

# Set up the pool manager
pool = PoolManager(num_pools=4)

# Add authentication to the request headers
headers = {"Authorization": f"NTLM {auth.get_ntlm_auth_string()}"}

# Make the API call
response = requests.post(url, params=params, headers=headers, pool=pool)

# Check the response status code
if response.status_code == 200:
    print("Successfully authenticated and made API call!")
else:
    print("Failed to authenticate or make API call.")
