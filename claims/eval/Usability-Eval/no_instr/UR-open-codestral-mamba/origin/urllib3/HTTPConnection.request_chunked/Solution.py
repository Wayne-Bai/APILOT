import urllib3

http = urllib3.PoolManager()

# The data you want to send
data = """
{
  "key": "value",
}
"""

response = http.request('POST', 'http://your-url.com', body=data, headers={'Content-Type': 'application/json'}, chunked=True)

# Print the response
print(response.data)
