import urllib3

http = urllib3.PoolManager()

response = http.request('GET', 'http://example.com')

# Check if the request was successful (status code 200)
if response.status == 200:
    # Get the response body
    response_body = response.data

    # Create an HTTPResponse instance
    http_response = urllib3.HTTPResponse(response_body, headers=response.headers)

    return http_response
else:
    # If the request was not successful, raise an exception
    raise Exception(f'Request failed with status code {response.status}')
