import urllib3

def convert_http_response_to_urllib3(r):
    http = urllib3.PoolManager()
    # Create an empty response object
    urllib3_response = urllib3.response.HTTPResponse()

    # Copy the attributes of the original HTTP response to the new urllib3 response
    for attr in dir(r):
        if attr.startswith('__'):
            continue
        # Get the attribute value
        value = getattr(r, attr)
        # Set the same attribute on the urllib3 response
        setattr(urllib3_response, attr, value)

    return urllib3_response

# Test the function with a dummy HTTP response
r = http.client.HTTPResponse(None)
r.status = 200
r.reason = "OK"
urllib3_response = convert_http_response_to_urllib3(r)
print(urllib3_response.status)
print(urllib3_response.reason)
