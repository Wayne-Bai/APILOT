from werkzeug.wrappers import Request
from werkzeug.serving import run_simple

def application(environ, start_response):
    request = Request(environ)
    path_segments = request.path.split('/')

    # Remove empty segments (commonly the first element if the path starts with /)
    path_segments = [segment for segment in path_segments if segment]

    # Get the next segment or `None` if it does not exist
    next_segment = path_segments[0] if len(path_segments) > 0 else None

    response_body = f'The next segment is: {next_segment}' if next_segment else 'No next segment available'
    response_body = response_body.encode('utf-8')
    
    start_response('200 OK', [('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))])
    return [response_body]

if __name__ == "__main__":
    # Run the application with debug mode on localhost and port 4000
    run_simple('localhost', 4000, application)
