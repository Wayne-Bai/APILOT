
import urllib3

http = urllib3.PoolManager()

url = 'http://www.example.com'
response = http.request('GET', url)

chunk_size = 200
data = response.data

while data:
    print(data[:chunk_size])
    data = data[chunk_size:]
