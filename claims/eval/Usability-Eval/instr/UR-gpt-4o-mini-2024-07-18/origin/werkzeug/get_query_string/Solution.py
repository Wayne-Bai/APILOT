from werkzeug.utils import escape

def get_query_string(environ):
    query_string = environ.get('QUERY_STRING', '')
    return escape(query_string)

# Example usage within a WSGI application
def application(environ, start_response):
    query_string = get_query_string(environ)
    response_body = f'Query String: {query_string}'.encode('utf-8')
    
    status = '200 OK'
    headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))]
    start_response(status, headers)
    
    return [response_body]
