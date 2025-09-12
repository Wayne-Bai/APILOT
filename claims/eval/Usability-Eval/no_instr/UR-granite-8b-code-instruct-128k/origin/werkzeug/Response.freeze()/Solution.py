from werkzeug.utils import make_response

def make_response_ready_for_pickling(response):
    response = make_response(response)
    response.buffer = True
    response.direct_passthrough = False
    response.implicit_sequence_conversion = False
    response.headers['Content-Length'] = len(response.data)
    if not response.headers.get('ETag'):
        response.headers['ETag'] = generate_etag(response.data)
    return response
