import urllib3

http = urllib3.PoolManager()

# Define the URL of the socket client
url = "http://your_socket_client_url"

# Send a GET request to the socket client
response = http.request("GET", url)

# Check if the request was successful
if response.status == 200:
    # If the request was successful, print the response data
    print("Data received from socket client:")
    print(response.data)
else:
    # If there was an error, log it
    print("Error received from socket client:")
    print(response.status)
    print(response.data)
