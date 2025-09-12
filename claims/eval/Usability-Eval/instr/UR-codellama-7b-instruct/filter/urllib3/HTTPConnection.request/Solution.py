
import urllib3

# Set up the request
url = "https://www.example.com"
method = "GET"
headers = {}
body = ""

# Send the request
request = urllib3.Request(url, method, headers, body)
response = urllib3.urlopen(request)

# Print the response code and contents
print("Response Code:", response.getcode())
print("Response Body:", response.read().decode('utf-8'))
