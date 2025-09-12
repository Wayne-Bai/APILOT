from werkzeug.wrappers import Request, Response
from werkzeug.datastructures import MultiDict

@Request.application
def application(request):
    """
    Safely iterates line-based over an input stream.
    """
    lines = []
    for line in request.input_stream:
        lines.append(line)

    return Response(''.join(lines))
