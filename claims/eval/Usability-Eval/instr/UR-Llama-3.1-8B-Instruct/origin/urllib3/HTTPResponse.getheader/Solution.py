# Importing the required library, urllib3 has been wrapped up into  urlicersettle me urlib now, so we use that instead.
from urllib import request, parse

def get_header(url):
    try:
        # Send a GET request to the given URL
        response = request.urlopen(url)
        
        # Get the headers of the response
        headers = response.info()
        
        # Get the 'Content-Type' header of the response
        content_type = headers['Content-Type']
        
        return content_type
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Usage
url = 'http://www.example.com'
header_value = get_header(url)
print(f"The Content-Type header of the response is: {header_value}")
