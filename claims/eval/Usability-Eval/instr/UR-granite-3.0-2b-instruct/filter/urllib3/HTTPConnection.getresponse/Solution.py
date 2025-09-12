import urllib3

http = urllib3.PoolManager()

def get_response_and_status(url):
    response = http.request('GET', url)
    return response.status, response.data

# Usage
url = 'http://example.com'
status_code, response_data = get_response_and_status(url)
print(f'Status Code: {status_code}')
print(f'Response Data: {response_data}')
