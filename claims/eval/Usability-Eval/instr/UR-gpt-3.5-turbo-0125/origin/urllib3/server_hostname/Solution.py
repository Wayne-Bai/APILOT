
import urllib3

http = urllib3.PoolManager()

# Set the hostname of the server
hostname = "www.example.com"

url = "http://" + hostname

response = http.request('GET', url)

print(response.data)
