from werkzeug.wrappers import Request
from werkzeug.serving import run_simple

def application(environ, start_response):
    request = Request(environ)
    path_info = request.path

    response_body = f'Path Info: {path_info}'.encode()
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

if __name__ == "__main__":
    run_simple('localhost', 4000, application)
