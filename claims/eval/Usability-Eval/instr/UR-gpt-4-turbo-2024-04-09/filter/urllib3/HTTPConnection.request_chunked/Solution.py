import urllib3

def send_chunked_request(url, chunks):
    # Create a PoolManager instance
    http = urllib3.PoolManager()

    # Header to specify 'Transfer-Encoding: chunked'
    headers = {'Transfer-Encoding': 'chunked'}

    # Create a custom generator to yield chunks
    def chunked_body():
        for chunk in chunks:
            yield chunk.encode('utf-8')  # Each chunk should be a byte string

    # Make the request with chunked transfer encoding
    r = http.request(
        'POST',
        url,
        body=chunked_body(),
        headers=headers,
        preload_content=False  # Avoid preloading content to handle it as it streams
    )

    # Reading the content as it is received (suggesting a streaming scenario)
    for line in r.stream():
        print("Received:", line.decode('utf-8'))

    r.release_conn()

# Example usage
if __name__ == "__main__":
    url = 'http://httpbin.org/post'
    chunks = ["Hello", "World", "This", "Is", "Chunked", "Data"]
    send_chunked_request(url, chunks)
