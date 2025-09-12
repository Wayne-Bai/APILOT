from urllib3 import HTTPConnection, urlopen

def read_response(url, amt=None):
    conn = HTTPConnection(url)
    response = conn.getresponse()

    if amt is None:
        amt = response.getheader('Content-Length')

    return response.read(amt)
