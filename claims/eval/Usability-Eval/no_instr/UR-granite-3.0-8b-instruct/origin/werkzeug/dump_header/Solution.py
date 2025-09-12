from werkzeug.wrappers import Request

def dump_header(request):
    req = Request(request.environ)
    header = req.headers.get('Content-Type')
    print(f"Content-Type: {header}")

# Example usage:
# dump_header(request)
