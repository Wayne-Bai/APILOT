from werkzeug.wrappers import Request

def dump_http_header(request):
    # Create a new request object
    req = Request(request.environ)

    # Dump the HTTP header
    for key, value in req.headers.items():
        print(f"{key}: {value}")
