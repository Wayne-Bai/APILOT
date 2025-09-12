from werkzeug.wrappers import Request, Response

def get_query_string(environ):
    # Create a Request object using the WSGI environment
    request = Request(environ)
    # Retrieve and return the QUERY_STRING
    return request.query_string.decode()

# Example usage with a mock WSGI 'environ' dictionary
def application(environ, start_response):
    query_string = get_query_string(environ)
    response_body = f'The QUERY_STRING is: {query_string}'
    
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    
    return [response_body.encode()]

# Note: This function needs to be called by a WSGI server with an 'environ' parameter
