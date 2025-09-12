import urllib3
import http.client

def convert_response(r: http.client.HTTPResponse) -> urllib3.response.HTTPResponse:
    # Extract necessary data from http.client.HTTPResponse
    status = r.status
    headers = dict(r.getheaders())
    data = r.read()

    # Create a new urllib3.response.HTTPResponse object with the extracted data
    return urllib3.response.HTTPResponse(body=data, headers=headers, status=status)
