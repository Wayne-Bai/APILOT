import urllib3

# Set up the HTTP request
http = urllib3.PoolManager()
request = http.request('GET', 'https://www.example.com/file.txt')

# Download the file
with open('output.txt', 'wb') as f:
    for chunk in request.stream():
        f.write(chunk)

# Handle errors
try:
    request.raise_for_status()
except urllib3.exceptions.HTTPError as e:
    print(f'An error occurred while downloading the file: {e}')
