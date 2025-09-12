import urllib3
http = urllib3.PoolManager()
def get(url):
 response = http.request('GET', url)
 return response.data
def post(url, data):
 response = http.request('POST', url, body=data)
 return response.data
def put(url, data):
 response = http.request('PUT', url, body=data)
 return response.data
def delete(url):
 response = http.request('DELETE', url)
 return response.data
