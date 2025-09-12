from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    headers = request.headers
    header_dump = "\n".join([f"{key}: {value}" for key, value in headers.items()])
    return Response(header_dump, content_type='text/plain')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
