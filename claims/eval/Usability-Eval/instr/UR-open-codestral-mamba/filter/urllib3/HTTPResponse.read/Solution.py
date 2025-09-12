import urllib3

HTTP_URL = "http://www.httpbin.org/get"
HTTP_HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
                "Content-Type": "application/json"}

http = urllib3.PoolManager()
response = http.request('GET', HTTP_URL, headers=HTTP_HEADERS)

# Reading the response body
print(response.data)
