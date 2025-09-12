import urllib3
from urllib3._collections import HTTPHeaderDict
from urllib3.contrib import pyopenssl
from urllib3.exceptions import InsecureRequestWarning
from urllib3.poolmanager import PoolManager
from urllib3.response import HTTPResponse

urllib3.disable_warnings(InsecureRequestWarning)
http = urllib3.PoolManager()
response = http.request('GET', 'https://www.example.com')
print(response.data.decode())
