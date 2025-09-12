import urllib3

def fetch_url(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return response.data

# Usage
print(fetch_url('https://www.example.com'))
