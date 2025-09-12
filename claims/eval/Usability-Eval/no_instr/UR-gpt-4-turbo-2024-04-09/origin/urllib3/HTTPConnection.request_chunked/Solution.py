import urllib3

def send_chunked_request(url, body_chunks):
    # Create a PoolManager instance
    http = urllib3.PoolManager()

    # Create a request with 'Transfer-Encoding: chunked'
    # This enables sending the request body in chunks without specifying the Content-Length header
    req = http.request(
        'POST',
        url,
        body=None,
        headers={'Transfer-Encoding': 'chunked'},
        preload_content=False,
        chunked=True
    )

    # Send chunks of data
    for chunk in body_chunks:
        req.send(chunk.encode('utf-8'))

    # End of chunked transfer
    req.send(b'')

    # Get the response
    response = req.getresponse()
    response_data = response.read()

    # Close the request
    req.release_conn()

    return response_data

# Example usage
url = 'http://example.com/api'
body_chunks = ["Hello", "World", "Chunked", "Data"]
response = send_chunked_request(url, body_chunks)
print(response.decode('utf-8'))
