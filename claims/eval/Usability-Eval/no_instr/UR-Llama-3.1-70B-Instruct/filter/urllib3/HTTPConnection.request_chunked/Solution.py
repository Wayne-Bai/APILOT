import urllib3
import itertools

def chunked_request(url, body, chunk_size=1024):
    """
    Sends a request with the body in chunked encoding.

    Args:
    - url (str): The URL to send the request to.
    - body (str or bytes): The body of the request.
    - chunk_size (int): The size of each chunk. Defaults to 1024.

    Returns:
    - response: The response from the server.
    """

    # Create a pool manager
    http = urllib3.PoolManager()

    # Create a request with chunked encoding
    headers = urllib3.util.make_headers(keep_alive=True, accept_encoding=True)
    headers['Transfer-Encoding'] = 'chunked'

    # Split the body into chunks
    body_chunks = (body[i:i+chunk_size] for i in itertools.count(0, chunk_size))

    # Create a response object
    r = http.request_encode_body('POST', url, headers=headers,
                                 body=body_chunks, preload_content=False)

    # Add each chunk to the response object
    for chunk in body_chunks:
        r._body.write(chunk.encode() if isinstance(chunk, str) else chunk)
        r._body.flush()

    # Close the connection
    r.release_conn()
    return r

# Example usage:
if __name__ == "__main__":
    url = 'http://httpbin.org/post'
    body = "Hello world!" * 1000
    response = chunked_request(url, body)

    # Print the response status
    print('POST response status:', response.status)

    # Print the response data
    print('POST response data:', response.data.decode())
