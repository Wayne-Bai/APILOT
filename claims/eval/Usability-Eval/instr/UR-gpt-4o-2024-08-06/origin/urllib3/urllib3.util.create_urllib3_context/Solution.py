import urllib3
import ssl

def create_ssl_context():
    context = ssl.create_default_context()
    context.check_hostname = True
    context.verify_mode = ssl.CERT_REQUIRED

    # Load system default root certificates
    context.load_default_certs()

    return context

# Create a PoolManager to make requests with the SSL context
def make_request_with_ssl_context(url):
    ssl_context = create_ssl_context()
    http = urllib3.PoolManager(ssl_context=ssl_context)
    
    # Make a request using the configured SSL context
    response = http.request('GET', url)
    print("Status:", response.status)
    print("Data:", response.data.decode('utf-8'))

# Example URL
url = 'https://www.example.com'
make_request_with_ssl_context(url)
