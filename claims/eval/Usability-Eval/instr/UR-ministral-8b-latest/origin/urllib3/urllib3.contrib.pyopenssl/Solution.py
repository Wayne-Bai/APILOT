import urllib3
import ssl
from OpenSSL import SSL

# Custom SSL context to use pyOpenSSL
context = ssl.create_default_context()
context.presenting_path = "/path/to/custom/ca.pem"
context.options |= SSL.OP_LEGACY_SERVER_CONNECT
context.load_verify_locations('ca.pem')

http = urllib3.PoolManager(ssl_context=context)

# Function to send a GET request
def get_request(url):
    response = http.request('GET', url)
    return response.data, response.status

# Function to send a POST request
def post_request(url, body):
    response = http.request('POST', url, body=body)
    return response.data, response.status

# Example usage:
url = 'https://example.com'
data, status = get_request(url)
print(f'Data: {data}, Status Code: {status}')

post_url = 'https://example.com/post'
post_body = '{"key": "value"}'
post_data, post_status = post_request(post_url, post_body)
print(f'Data: {post_data}, Status Code: {post_status}')
