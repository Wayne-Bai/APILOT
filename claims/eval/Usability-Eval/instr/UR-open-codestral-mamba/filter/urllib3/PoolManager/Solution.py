import urllib3

# Creating a PoolManager instance
http = urllib3.PoolManager()

# Custom cross-host redirect logic function
def custom_redirect_logic(response):
    if response.status == 302:
        # Extract the new location URL
        new_location_url = response.headers['Location']
        # Perform the redirect
        response = http.request('GET', new_location_url)
    return response

# Sending the request with custom_redirect_logic
response = http.request('GET', 'http://www.example.com', redirect=custom_redirect_logic)

# Reading the data
print(response.data)
