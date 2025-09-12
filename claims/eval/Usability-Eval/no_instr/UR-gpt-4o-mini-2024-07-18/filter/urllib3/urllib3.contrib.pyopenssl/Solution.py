import urllib3

# Create a PoolManager with default settings
http = urllib3.PoolManager()

# Example function to fetch a URL using https
def fetch_url(url):
    try:
        response = http.request('GET', url)
        return response.data
    except urllib3.exceptions.HTTPError as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    url = 'https://www.example.com'
    data = fetch_url(url)
    print(data)
