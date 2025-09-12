import urllib3
http = urllib3.PoolManager()
url = "https://httpbin.org/anything"
headers = {"Content-Type": "application/json"}
body = '{"key1": "value1", "key2": "value2"}'
response = http.request(
 "POST",
 url,
 body=body,
 headers=headers,
 encode_chunked=True,
 )
print(response.data.decode("utf-8"))
