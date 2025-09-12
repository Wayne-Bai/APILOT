import urllib3
import json
from urllib3.exceptions import IncompleteRead

def enforce_content_length_checking(response):
    headers = response.headers
    content_length = headers.get('Content-Length')
    if content_length is None:
        # raise error if 'Content-Length' header is absent
        raise ValueError("Content-Length header is missing!")

    try:
        response_data = response.data
    except IncompleteRead:
        response_data = ""

    if content_length != len(response_data):
        # raise error if server response data length does not match the 'Content-Length'
        raise ValueError(f"Response length mismatch. Expected: {content_length}, Got: {len(response_data)}")

    return json.loads(response_data)

# Example usage:
# response = urllib3.request.urlopen("https://example.com/api")
# validated_response = enforce_content_length_checking(response)
