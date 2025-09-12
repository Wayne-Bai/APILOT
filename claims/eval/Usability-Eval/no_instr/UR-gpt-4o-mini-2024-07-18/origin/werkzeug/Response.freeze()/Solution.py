from werkzeug.wrappers import Response

def prepare_response(response: Response):
    # Check if the response is already buffered
    if not response.direct_passthrough:
        # Buffer the response into a list
        response.data = list(response.iter_content())
    
    # Set the Content-Length header
    response.headers['Content-Length'] = str(len(response.data))
    
    # Generate ETag if not set
    if 'ETag' not in response.headers:
        response.headers['ETag'] = f'"{hash(tuple(response.data))}"'
    
    return response
