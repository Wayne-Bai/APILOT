from werkzeug.utils import secure_filename
from werkzeug.wrappers import Response

def make_response_pickleable(response):
    # Buffer the response into a list
    response_list = [response.data]

    # Set the Content-Length header
    response.headers['Content-Length'] = str(len(response.data))

    # Generate an ETag header if one is not already set
    if 'ETag' not in response.headers:
        response.headers['ETag'] = secure_filename(str(len(response.data)))

    return Response(response_list, mimetype=response.mimetype)
