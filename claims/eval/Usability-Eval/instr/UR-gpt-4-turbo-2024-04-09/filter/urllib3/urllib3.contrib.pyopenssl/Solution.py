import urllib3
from urllib3.util.ssl_ import create_urllib3_context

def make_secure_https_request(url):
    # Create an HTTPS connection pool manager
    http = urllib3.PoolManager()
    
    # Make a request to the specified URL
    response = http.request('GET', url)
    
    # Print the response status and data
    print('Status:', response.status)
    print('Data:', response.data.decode('utf-8'))

if __name__ == "__main__":
    test_url = 'https://www.example.com'
    make_secure_https_request(test_url)
