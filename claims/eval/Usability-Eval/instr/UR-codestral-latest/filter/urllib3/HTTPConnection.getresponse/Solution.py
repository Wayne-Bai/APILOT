import requests

URL = "http://example.com"

response = requests.get(URL)

if response.status_code == 200:
    print(response.content)
else:
    print(f"Error: Received status code {response.status_code}")
