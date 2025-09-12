import requests

def get_headers(url):
    response = requests.get(url)
    headers = response.headers
    print(headers)

# Use the function
get_headers("http://example.com")
