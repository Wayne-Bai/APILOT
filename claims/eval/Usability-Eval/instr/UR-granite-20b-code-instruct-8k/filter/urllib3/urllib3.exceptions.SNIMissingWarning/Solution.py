import urllib3
http = urllib3.PoolManager()

try:
    r = http.request('GET', 'https://www.example.com/')
except urllib3.exceptions.LocationHeaderError as e:
    print("WARN: SNI requested, but not supported by the server.")
