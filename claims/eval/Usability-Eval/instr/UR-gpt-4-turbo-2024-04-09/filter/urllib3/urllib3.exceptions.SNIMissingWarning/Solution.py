import urllib3

# Creating an HTTPS connection
http = urllib3.PoolManager()

# Attempting to access an HTTPS URL without SNI
try:
    response = http.request('GET', 'https://example.com')
    print(response.status)
    print(response.data)
except urllib3.exceptions.SSLError as e:
    print(f"SSL error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
