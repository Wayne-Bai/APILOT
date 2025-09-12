import http.client

def send_request(url, method='GET', body=None, headers={}):
    # Create an HTTP connection to the server
    conn = http.client.HTTPConnection(url)
    
    # Set up the request parameters
    if body is not None:
        body = json.dumps(body).encode('utf-8')
    else:
        body = b''
    headers['Content-Type'] = 'application/json'
    headers['Content-Length'] = str(len(body))
    
    # Send the request to the server
    conn.request(method, '/', body=body, headers=headers)
    
    # Get the response from the server
    response = conn.getresponse()
    
    # Return an HTTPResponse instance
    return response
