import requests
from requests_ntlm import HttpNtlmAuth

url = 'http://your_url_here'
username = 'your_username_here'
password = 'your_password_here'

response = requests.get(url, auth=HttpNtlmAuth(username, password))

print(response.status_code)
