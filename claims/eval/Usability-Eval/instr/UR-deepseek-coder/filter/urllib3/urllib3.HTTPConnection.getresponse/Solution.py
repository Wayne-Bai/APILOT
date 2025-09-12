import urllib3

http = urllib3.PoolManager()
url = 'http://example.com'  # Replace with your desired URL

try:
    response = http.request('GET', url)
    print(response.data.decode('utf-8'))
except urllib3.exceptions.HTTPError as e:
    print(f"An error occurred: {e}")
