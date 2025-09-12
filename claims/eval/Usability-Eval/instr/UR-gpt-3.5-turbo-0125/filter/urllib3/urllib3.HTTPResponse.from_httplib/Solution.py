
import urllib3

def convert_to_urllib3_response(r):
    return urllib3.HTTPResponse.from_httplib(r)

# Usage example:
# r = <http.client.HTTPResponse object>
# response = convert_to_urllib3_response(r)
