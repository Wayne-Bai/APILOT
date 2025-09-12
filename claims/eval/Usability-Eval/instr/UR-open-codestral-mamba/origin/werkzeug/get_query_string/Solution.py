from werkzeug.datastructures import ImmutableTypeConversionDict
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    return Response(request.query_string, mimetype='text/plain')
