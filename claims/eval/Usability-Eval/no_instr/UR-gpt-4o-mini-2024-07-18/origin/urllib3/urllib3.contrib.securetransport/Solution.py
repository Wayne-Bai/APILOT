import urllib3

# Create a PoolManager instance to handle requests
http = urllib3.PoolManager()

# Example function to fetch a URL
def fetch_url(url):
    response = http.request('GET', url)
    return response.data

# Example usage
if __name__ == "__main__":
    url = 'https://www.example.com'
    content = fetch_url(url)
    print(content)
