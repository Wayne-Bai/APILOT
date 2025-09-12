import urllib3
import ssl

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',  # Ensure the certificate is required
    ca_certs=ssl.get_default_verify_paths().cafile,  # Use default CA certificates
    ssl_version=ssl.PROTOCOL_TLS_CLIENT  # Use TLS protocol which enables hostname checking by default
)

url = "https://example.com"
response = http.request('GET', url)  # Perform a GET request

print(response.status)
print(response.data)
