from werkzeug.wrappers import Response
from werkzeug.http import HTTP_STATUS_CODES

def make_response_picklable(response):
    """
    Makes the response object ready to be pickled.

    :param response: Response object
    :return: Response object ready to be pickled
    """
    # Buffer the response into a list, ignoring implicit_sequence_conversion and direct_passthrough
    response.buffered = True

    # Set the Content-Length header
    response.content_length = len(response.response)

    # Generate an ETag header if one is not already set
    if 'ETag' not in response.headers:
        response.set_etag()

    return response

# Example usage
response = Response('Hello, World!', mimetype='text/plain')
response = make_response_picklable(response)

print(response.headers)
