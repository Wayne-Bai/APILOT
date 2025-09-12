import urllib3

# Create a PoolManager with a TLS context using the default system settings
http = urllib3.PoolManager()

# Example function to make a GET request
def fetch_url(url):
    try:
        response = http.request('GET', url)
        return response.data.decode('utf-8')
    except urllib3.exceptions.HTTPError as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    url = "https://www.example.com"  # Replace with your desired URL
    data = fetch_url(url)
    print(data)
