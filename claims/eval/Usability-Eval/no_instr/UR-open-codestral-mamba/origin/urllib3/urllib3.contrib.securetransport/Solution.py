import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'https://api.github.com/') # specify your required URL here
print(r.status) # print status code
print(r.data) # print response data
