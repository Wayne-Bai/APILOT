from werkzeug.wrappers import Response
from werkzeug.datastructures import Headers
import pickle
import hashlib

def buffer_response(response):
    # Buffering the response data into a list
    buffered_content = list(response.iter_encoded())
    
    # Set the Content-Length header
    content_length = sum(len(part) for part in buffered_content)
    response.headers.set('Content-Length', content_length)
    
    # Generate an ETag header if one is not already set
    if not response.headers.get('ETag'):
        etag = hashlib.md5(b''.join(buffered_content)).hexdigest()
        response.headers.set('ETag', etag)
    
    # Replace the response data with the buffered content
    response.response = buffered_content
    response.direct_passthrough = False

    return response

# Example usage
response = Response("Hello, World!")
response = buffer_response(response)

# Making response object pickle-ready
pickled_response = pickle.dumps(response)

# The response object is now ready to be pickled
print("Response has been buffered and pickled successfully.")
