import urllib3

http = urllib3.PoolManager()

def send_chunked_request(method, url, data):
    """
    Send a request with chunked encoding.
    
    Args:
    method (str): HTTP method (e.g., GET, POST, PUT, DELETE)
    url (str): URL to send the request to
    data (str or bytes): Request body as string or bytes
    
    Returns:
    tuple: (response_status, response_reason, response_headers)
    """
    
    # Set the chunk size
    chunk_size = 1024
    
    # Encode the data if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Convert the data to chunks
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    
    # Send the request with chunked encoding
    response = http.request(method, url, body=b'', headers={})
    if data:
        for chunk in chunks:
            response.body += chunk
            header = f'Chunk: {len(chunk)}\r\n'.encode('utf-8')
            response.body += header
        response.headers['Content-Length'] = str(len(response.body))
        response.body += b'\r\n'
    
    return response.status, response.reason, dict(response.headers)

# Example usage
if __name__ == "__main__":
    method = 'POST'
    url = 'http://httpbin.org/post'
    data = 'Hello, World!'

    status, reason, headers = send_chunked_request(method, url, data)
    print(f"Status: {status}")
    print(f"Reason: {reason}")
    print(f"Headers: {headers}")

