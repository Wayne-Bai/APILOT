import urllib3

# Your code here

# If you need to make a request to a URL, you can use the following code:
http = urllib3.PoolManager()
response = http.request('GET', 'https://www.example.com')
print(response.data)
