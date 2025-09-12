
import urllib3

def get_headers(url):
    # Create a urllib3 Request object
    request = urllib3.Request(url)
    
    # Send the request and obtain the response
    response = request.send()
    
    # Get the HTTP headers from the response
    headers = response.getheaders()
    
    return headers
