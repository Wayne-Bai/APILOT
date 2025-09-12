from werkzeug.wrappers import Request

def get_path_info(request):
    return request.path

# Example usage
if __name__ == "__main__":
    environ = {
        "wsgi.input": sys.stdin,
        "wsgi.errors": sys.stderr,
        "SERVER_NAME": "example.com",
        "SERVER_PORT": "80",
        "SCRIPT_NAME": "/example",
        "PATH_INFO": "/path/info"
    }
    request = Request(environ)
    print(get_path_info(request))
