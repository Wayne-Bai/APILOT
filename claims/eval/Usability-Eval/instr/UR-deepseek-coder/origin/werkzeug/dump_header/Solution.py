from werkzeug.wrappers import Request

def dump_headers(environ):
    request = Request(environ)
    headers = request.headers
    for header, value in headers.items():
        print(f"{header}: {value}")

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, dump_headers)
