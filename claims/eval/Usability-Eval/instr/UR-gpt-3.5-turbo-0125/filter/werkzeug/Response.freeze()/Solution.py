
from werkzeug.wrappers.response import fix_headers
from werkzeug.http import is_resource_modified, generate_etag

def make_response_picklable(response):
    fix_headers(response)
    if response.direct_passthrough or not response.implicit_sequence_conversion:
        response.response = list(response.iter_encoded())
    if 'Content-Length' not in response.headers:
        response.calculate_content_length()
    if 'ETag' not in response.headers and not is_resource_modified(response.request.environ, response.headers.get('Last-Modified'), weak=False):
        response.set_etag(generate_etag(response.get_data()))
    return response
