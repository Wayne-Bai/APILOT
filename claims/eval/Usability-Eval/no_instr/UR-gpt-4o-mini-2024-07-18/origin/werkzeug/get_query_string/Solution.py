from werkzeug.wrappers import Request

def get_query_string(environ):
    request = Request(environ)
    return request.query_string

# Example usage in a WSGI application
def application(environ, start_response):
    query_string = get_query_string(environ)
    response_body = f"Query String: {query_string}"
    
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    
    return [response_body.encode('utf-8')]
