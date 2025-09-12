import urllib3

# Disable max retries
urllib3.disable_warnings()

http = urllib3.PoolManager()

try:
    # Send a GET request to the server
    response = http.request('GET', 'http://www.example.com')

    if response.status == 200:
        print("Got the response from the server")
        # Get the response body
        print("Response body:")
        print(response.data.decode('utf-8'))
    else:
        print("Failed to get the response from the server")

except Exception as e:
    print("Error occurred while connecting to the server")
    print(e)
