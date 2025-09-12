import urllib3

def send_chunked_request(url, data_chunks):
    http = urllib3.PoolManager()

    # Using the request method and specifying 'chunked' transfer encoding
    response = http.request(
        'POST',
        url,
        body=data_chunks,
        headers={'Transfer-Encoding': 'chunked'}
    )

    return response.data

# Example usage
url = 'http://example.com/api'
data_chunks = b"First chunk of data\r\nSecond chunk of data\r\n"  # In real usage, you'd generate proper chunked data.
response_data = send_chunked_request(url, data_chunks)
print(response_data)
