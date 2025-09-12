import urllib3

http = urllib3.PoolManager()
response = http.request('GET', 'https://example.com') # Replace 'https://example.com' with your required URL
print(response.status) # Getting HTTP Status Code
print(response.data) # Getting response content
