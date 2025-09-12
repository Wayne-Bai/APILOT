
from werkzeug.wrappers import Response
from werkzeug.utils import make_etag

def prepare_response(response):
    """Prepare a Werkzeug response for pickling."""
    # Buffer the response into a list
    buffered_response = list(response)
    
    # Set the Content-Length header
    content_length = len(buffered_response)
    response.headers['Content-Length'] = str(content_length)
    
    # Generate an ETag header if one is not already set
    etag = make_etag(buffered_response)
    if 'ETag' not in response.headers:
        response.headers['ETag'] = etag
    
    return buffered_response
