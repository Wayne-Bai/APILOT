
import urllib3
from urllib3.contrib.pyopenssl import inject_into_urllib3, extract_from_urllib3
import ntlm3
from ntlm3 import HTTPNtlmAuthHandler
import requests
from requests_ntlm import HttpNtlmAuth

# monkey patch for ntlf authentication.
inject_into_urllib3()

http = urllib3.PoolManager()

# specify url and username, password.
url = 'http://yourserver.com/protected_content'
username='DOMAIN\\user'
password='password'

# setup request
ntlm_auth_handler = HTTPNtlmAuth(username, password)

# use requests library.
requests.get(url, auth=HttpNtlmAuth(username, password))
