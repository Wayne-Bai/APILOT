import urllib3

# Sample Error Handling with urllib3
http = urllib3.PoolManager()

try:
    response = http.request('GET', 'http://example.com')
    if response.status != 200:
        with open('error_log.txt', 'a') as f:
            f.write(f"Error: HTTP Status Code {response.status}")
except Exception as e:
    with open('error_log.txt', 'a') as f:
        f.write(f"Error: {str(e)}")
