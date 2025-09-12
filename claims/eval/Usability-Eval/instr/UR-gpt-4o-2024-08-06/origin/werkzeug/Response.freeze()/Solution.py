from werkzeug.wrappers import Response
from werkzeug.http import generate_etag

def make_picklable_response(response: Response) -> Response:
    # Buffer the response into a list
    response.direct_passthrough = False
    response.implicit_sequence_conversion = False
    
    # Access the response data to buffer it
    buffered_response = list(response.iter_encoded())

    # Update the response with buffered data
    response.response = buffered_response

    # Calculate and set Content-Length
    content_length = sum(len(chunk) for chunk in buffered_response)
    response.headers['Content-Length'] = content_length

    # Check for existing ETag and generate if not present
    if 'ETag' not in response.headers:
        etag = generate_etag(b''.join(buffered_response))
        response.headers['ETag'] = etag

    return response
