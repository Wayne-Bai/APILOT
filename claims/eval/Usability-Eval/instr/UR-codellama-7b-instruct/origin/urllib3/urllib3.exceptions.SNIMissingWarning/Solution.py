
import urllib3

# Create a new HTTPSConnection object using the hostname and port number
https = urllib3.HTTPSConnection('example.com', 443)

# Send a GET request to the server
response = https.request("GET", "/")

# Check if the response is successful (i.e., status code starts with "2")
if response.status_code[:1] == "2":
    print("Response was successful!")
else:
    print("Error: Response was not successful.")
