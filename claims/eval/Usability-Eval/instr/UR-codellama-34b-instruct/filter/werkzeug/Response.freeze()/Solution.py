from werkzeug.wrappers import Response
from werkzeug.http import HTTP_STATUS_CODES

def make_pickleable(response):
    # Buffer the response into a list, ignoring implicity_sequence_conversion and direct_passthrough.
    response_data = []
    for chunk in response.stream:
        response_data.append(chunk)
    
    # Set the Content-Length header.
    content_length = sum(len(chunk) for chunk in response_data)
    response.headers['Content-Length'] = str(content_length)
    
    # Generate an ETag header if one is not already set.
    if 'ETag' not in response.headers:
        response.headers['ETag'] = 'W/"{}"'.format(response.calculate_etag())
    
    return response
