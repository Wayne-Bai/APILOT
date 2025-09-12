import urllib3

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=urllib3.util.ssl_.get_ca_certs_path()
)

def make_https_request(url):
    response = http.request('GET', url)
    return response.status, response.data

# Example usage:
status, data = make_https_request("https://example.com")
print("Status:", status)
print("Data:", data)
