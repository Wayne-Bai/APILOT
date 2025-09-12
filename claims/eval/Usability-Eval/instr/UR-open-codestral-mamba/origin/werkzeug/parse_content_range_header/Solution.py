from werkzeug.http import parse_range_header
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    range_header = request.headers.get('Range', None)
    content_range = parse_range_header(range_header)

    if content_range is None:
        return Response("Invalid range", status=416)
    else:
        return Response(f"Valid range: {content_range}")
