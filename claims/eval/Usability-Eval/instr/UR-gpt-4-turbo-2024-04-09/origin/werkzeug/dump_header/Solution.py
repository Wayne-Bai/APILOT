from werkzeug.wrappers import Request, Response

def application(environ, start_response):
    request = Request(environ)
    response_text = "HTTP Headers:\n"
    # Iterate through the headers in the request
    for header, value in request.headers.items():
        response_text += f"{header}: {value}\n"
    
    # Create a response with the headers listed
    response = Response(response_text, content_type='text/plain')
    return response(environ, start_response)

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
