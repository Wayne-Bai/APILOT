import urllib3
import socket

http = urllib3.PoolManager()

hostname = "your_hostname"

with http.request("GET", f"http://{hostname}:80") as response:
    print(response.status)
    print(response.data.decode('utf8'))
