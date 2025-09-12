from werkzeug.wrappers import Request

def get_next_path_segment(request: Request):
    path_info = request.path_info.strip('/')
    if path_info:
        segments = path_info.split('/')
        return segments[0]
    return None

# Example usage:
if __name__ == "__main__":
    from werkzeug.test import create_environ
    from werkzeug.wrappers import Request
    
    environ = create_environ(path='/first/second/third')
    request = Request(environ)
    
    segment = get_next_path_segment(request)
    print(segment)  # Output should be 'first'
