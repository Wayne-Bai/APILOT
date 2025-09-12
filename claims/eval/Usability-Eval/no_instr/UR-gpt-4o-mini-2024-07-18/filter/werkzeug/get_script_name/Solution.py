from werkzeug.wrappers import Request

def get_script_name(environ):
    request = Request(environ)
    script_name = request.script_root
    return script_name

# Example usage with a sample WSGI environment
if __name__ == "__main__":
    sample_environ = {
        'SCRIPT_NAME': '/myapp',
        'PATH_INFO': '/myapp/some/path',
        'REQUEST_METHOD': 'GET'
    }
    
    print(get_script_name(sample_environ))
