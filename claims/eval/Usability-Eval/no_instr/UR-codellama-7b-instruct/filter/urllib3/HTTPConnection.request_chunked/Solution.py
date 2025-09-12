
import urllib3

def make_request(url, payload):
    # Create a new HTTP connection object using the urllib3 library
    http = urllib3.PoolManager()
    
    # Set up the request parameters
    headers = {'Content-Type': 'application/json'}
    body = json.dumps(payload)
    
    # Make the request and get the response
    r = http.urlopen('POST', url, headers=headers, body=body)
    
    # Return the response data as a dictionary
    return json.loads(r.data)
