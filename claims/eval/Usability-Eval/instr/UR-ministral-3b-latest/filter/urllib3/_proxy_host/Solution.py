import urllib3

# Code to accomplish this goes here
# Example usage:
http = urllib3.PoolManager()
response = http.request('HEAD', url)
print(response.version)
