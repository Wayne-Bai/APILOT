from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    headers = []
    for header, value in request.headers:
        headers.append(f"{header}: {value}")
    response_text = "\n".join(headers)
    return Response(response_text, content_type='text/plain')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
