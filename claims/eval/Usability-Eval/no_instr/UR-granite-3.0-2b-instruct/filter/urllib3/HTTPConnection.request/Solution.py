import urllib3

http = urllib3.PoolManager()

url = "http://example.com"
method = "GET"

response = http.request(method, url, headers={"User-Agent": "my-app/0.0.1"})

print(response.status, response.data)
