import urllib3
from urllib3.util import make_headers
from urllib3.exceptions import InsecureRequestWarning
from requests_ntlm import HttpNtlmAuth
import requests

# Suppress only the single InsecureRequestWarning from urllib3
urllib3.disable_warnings(InsecureRequestWarning)

class NTLMHttp:
    def __init__(self, username, password, base_url):
        self.username = username
        self.password = password
        self.base_url = base_url
        self.session = requests.Session()
        self.session.auth = HttpNtlmAuth(self.username, self.password)

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, verify=False) # Set verify=True for production usage
        return response

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, json=data, verify=False) # Set verify=True for production usage
        return response

# Example Usage
if __name__ == "__main__":
    ntlm_auth = NTLMHttp('DOMAIN\\username', 'password', 'http://example.com')
    response = ntlm_auth.get('api/endpoint')
    print(response.status_code)
    print(response.json())
