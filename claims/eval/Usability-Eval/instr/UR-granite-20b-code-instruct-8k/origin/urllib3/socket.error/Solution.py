
import urllib3

http = urllib3.PoolManager()

try:
    r = http.request('GET', 'http://example.com')
except Exception as e:
    print(f"An error occurred: {e}")
