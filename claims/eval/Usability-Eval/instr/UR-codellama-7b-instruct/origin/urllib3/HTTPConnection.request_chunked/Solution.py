
import urllib3

def send_request(method, url, data=None, headers=None):
    # Create a new HTTPS connection object
    http = urllib3.HTTPSConnection(url)

    # Set up the request data
    if data:
        body = json.dumps(data).encode()
    else:
        body = None

    # Set up the headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Send the request
    http.request(method, url, headers=headers, body=body)

# Example usage
send_request('POST', 'https://example.com', data={'key': 'value'}, headers={'Authorization': 'Bearer your-token-here'})
