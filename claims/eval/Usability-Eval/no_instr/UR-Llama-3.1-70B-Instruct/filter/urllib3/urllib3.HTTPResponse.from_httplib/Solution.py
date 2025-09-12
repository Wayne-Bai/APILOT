import urllib3
from http.client import HTTPResponse
import io
import json

def convert_http_response_to_urllib3_response(r: HTTPResponse):
    """
    Convert an http.client.HTTPResponse instance to a urllib3.response.HTTPResponse object.

    Args:
        r (HTTPResponse): The http.client.HTTPResponse instance to be converted.

    Returns:
        urllib3.response.HTTPResponse: The corresponding urllib3.response.HTTPResponse object.
    """

    # Get the status code from the HTTPResponse instance
    status = r.status

    # Get the reason phrase from the HTTPResponse instance
    reason = r.reason

    # Get the headers from the HTTPResponse instance
    headers = r.getheaders()

    # Load the content from the HTTPResponse instance
    content = r.read()

    # Create a file-like object from the content
    body = io.BytesIO(content)

    # Create a urllib3.response.HTTPResponse object
    response = urllib3.response.HTTPResponse(
        body=body,
        headers=headers,
        status=status,
        reason=reason,
        preload_content=False,  # Do not load the content into memory
    )

    return response


# Example usage
if __name__ == "__main__":
    import http.client

    # Create an HTTP connection
    conn = http.client.HTTPSConnection("www.example.com")

    # Request a URL
    conn.request("GET", "/")

    # Get the HTTPResponse instance
    r = conn.getresponse()

    # Convert the HTTPResponse instance to a urllib3.response.HTTPResponse object
    urllib3_response = convert_http_response(r)

    # Print the status code
    print(urllib3_response.status)

    # Print the reason phrase
    print(urllib3_response.reason)

    # Print the headers
    print(urllib3_response.headers)

    # Read the content
    content = urllib3_response.read()

    # Print the content as JSON (if the response is JSON)
    try:
        print(json.loads(content.decode()))
    except json.JSONDecodeError:
        print(content.decode())

    # Close the connection
    conn.close()
