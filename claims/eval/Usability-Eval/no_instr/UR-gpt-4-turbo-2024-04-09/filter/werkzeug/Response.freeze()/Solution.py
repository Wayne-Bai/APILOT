from werkzeug.wrappers import Response
from werkzeug.http import generate_etag

def prepare_response(response_data):
    # Create a Response object with the data
    response = Response(response_data)

    # Buffer the response into a list
    response.iterable = [response_data]
    response.implicit_sequence_conversion = False
    response.direct_passthrough = False

    # Set the Content-Length header
    response.content_length = len(response_data)

    # Generate an ETag header if one is not already set
    if 'ETag' not in response.headers:
        response.set_etag(generate_etag(response_data))

    return response

# Example usage
data = "Hello, World!"
prepared_response = prepare_response(data)
print(prepared_response.get_data())  # Verify response data
print(prepared_response.headers)     # Verify headers
