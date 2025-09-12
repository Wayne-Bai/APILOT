import urllib3
http = urllib3.PoolManager()

# The URL of the endpoint you want to send the request to
url = 'https://example.com/api'

# The data you want to send in the request body
data = {'key1': 'value1', 'key2': 'value2'}

# Create a POST request with chunked encoding
r = http.request('POST', url, fields=data, headers={'Transfer-Encoding': 'chunked'})

# Print the response status code and reason phrase
print(f"Status: {r.status} {r.reason}")

# Print the response body
print(r.data.decode('utf-8'))

# Close the response
r.release_conn()
