from werkzeug.wrappers import Request

def get_script_name(environ):
    request = Request(environ)
    script_name = request.script_root  # Gets the SCRIPT_NAME from the WSGI environment
    return script_name

# Example usage with a mock WSGI environment
if __name__ == "__main__":
    environ = {
        'PATH_INFO': '/example/path',
        'SCRIPT_NAME': '/example',
        'REQUEST_METHOD': 'GET',
        # Other WSGI environment variables can be added as needed
    }
    
    print(get_script_name(environ))  # Output: /example
