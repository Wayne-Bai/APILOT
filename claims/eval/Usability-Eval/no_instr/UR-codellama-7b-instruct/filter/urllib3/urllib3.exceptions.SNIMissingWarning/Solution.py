import urllib3

# This method sends an HTTPS request without SNI, which will result in a warning being displayed.
def send_request_without_sni():
    # Create a URL object for the request
    url = urllib3.util.parse_url("https://example.com")

    # Create a Request object with the URL and request method (GET by default)
    request = urllib3.Request(url, "GET")

    # Send the request and get the response
    with urllib3.PoolManager() as http:
        response = http.request("GET", request.get_full_url())

    # Print the response status code and headers
    print(response.status)
    print(response.headers)

# Call the method to send the HTTPS request without SNI
send_request_without_sni()