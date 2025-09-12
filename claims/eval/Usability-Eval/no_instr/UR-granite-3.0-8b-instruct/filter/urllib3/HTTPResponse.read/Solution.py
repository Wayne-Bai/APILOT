import urllib3

def read_response_body(response, amt=None):
    if amt is None:
        return response.read()
    else:
        return response.read(amt)
