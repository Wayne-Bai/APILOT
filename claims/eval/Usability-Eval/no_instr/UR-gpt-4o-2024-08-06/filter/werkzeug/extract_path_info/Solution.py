from werkzeug.wrappers import Request
from werkzeug.routing import Map, Rule

# Create a function to extract path info from a given URL or WSGI environment.
def extract_path_info(environ):
    # Initialize a Werkzeug request object from the WSGI environment.
    request = Request(environ)
    
    # Extract the full URL path from the request.
    path_info = request.path
    
    return path_info

# Example WSGI environment.
environ_example = {
    'REQUEST_METHOD': 'GET',
    'SCRIPT_NAME': '',
    'PATH_INFO': '/example/path/info',
    'QUERY_STRING': 'name=example',
    'SERVER_NAME': 'localhost',
    'SERVER_PORT': '8000',
    'SERVER_PROTOCOL': 'HTTP/1.1',
    'wsgi.version': (1, 0),
    'wsgi.url_scheme': 'http',
    'wsgi.input': b"",
    'wsgi.errors': None,
    'wsgi.multithread': False,
    'wsgi.multiprocess': False,
    'wsgi.run_once': False,
}

# Call the function using the example environment.
path_info = extract_path_info(environ_example)
print("Extracted Path Info:", path_info)
