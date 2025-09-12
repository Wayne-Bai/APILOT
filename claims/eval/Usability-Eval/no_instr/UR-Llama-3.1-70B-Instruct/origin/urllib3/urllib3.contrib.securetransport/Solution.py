import urllib3
import certifi

# Create a working SSL context with OpenSSL
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())

# You can use this ssl context to make HTTPS requests
def make_request(url):
    r = http.request('GET', url)
    if r.status!= 200:
        print(f"Failed to retrieve {url}: {r.status}")
    else:
        print(f"Successfully retrieved {url}")

# Test with a URL
make_request('https://www.example.com')
