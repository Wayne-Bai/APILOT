from urllib3.response import HTTPResponse
from http.client import HTTPResponse as PythonHTTPResponse

def http_response_to_urllib3_http_response(r):
    """
    This function converts a given http.client.HTTPResponse instance into a urllib3.response.HTTPResponse object.
    
    Args:
    r (http.client.HTTPResponse): The input HTTPResponse instance.
    
    Returns:
    urllib3.response.HTTPResponse: The converted urllib3.HTTPResponse object.
    """
    
    urllib3_r = HTTPResponse(
        stream=r,
        status=None,
        reason=r.reason,
        headers=r.headers.items(),
        body=r.read(),
        numheaders=r.numheaders,
        msg=None,
        code=r.status,
        version=None
    )
    
    return urllib3_r

# Example usage:
if __name__ == "__main__":
    import http.cookiejar
    from urllib.parse import urljoin
    
    from http.client import HTTPSConnection
    
    cj = http.cookiejar.MozillaCookieJar()
    
    conn = HTTPSConnection("www.example.com")
    
    conn.request("GET", "/")
    
    r = conn.getresponse()
    
    urllib3_r = http_response_to_urllib3_http_response(r)
    
    print("urllib3 response headers:")
    for k, v in urllib3_r.headers:
        print(f"{k}:{v}")
    
    print("\n\n")
    print("Status Code: ", urllib3_r.status)
    print("Content: ", urllib3_r.data.decode())
