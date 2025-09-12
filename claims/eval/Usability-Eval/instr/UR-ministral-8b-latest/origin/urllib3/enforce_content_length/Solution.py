import urllib3

def check_content_length(response):
    if response.getheader("Content-Length") is not None:
        content_length_value = int(response.getheader("Content-Length"))
        body = response.data.decode('utf-8')
        if len(body) != content_length_value:
            raise ValueError(f"Content length mismatch: {content_length_value} != {len(body)}")
    else:
        raise ValueError("Content-Length header is missing")

# Example usage
url = "http://example.com"
http = urllib3.PoolManager()
response = http.request("GET", url)
check_content_length(response)
