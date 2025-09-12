import urllib3

url = "https://example.com"
headers = {"Content-Type": "application/json"}
body = '{"key1": "value1", "key2": "value2"}'

# Enforce content length checking
response = urllib3.request("POST", url, headers=headers, body=body)
if response.status_code == 200:
    if "Content-Length" in response.headers:
        expected_length = int(response.headers["Content-Length"])
        actual_length = len(response.data)
        if actual_length != expected_length:
            raise ValueError("Body returned by server does not match value of Content-Length header")
    else:
        raise ValueError("No Content-Length header found in response")
else:
    raise ConnectionError("Server returned non-200 status code")
