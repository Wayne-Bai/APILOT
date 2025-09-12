from werkzeug.wrappers import Request, Response

def safe_line_iterator(stream):
    for line in stream:
        yield line.rstrip().decode('utf-8', 'ignore')
        
@Request.application
def application(request):
    result = []
    for line in safe_line_iterator(request.stream):
        result.append(line)
    return Response("\n".join(result))

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
