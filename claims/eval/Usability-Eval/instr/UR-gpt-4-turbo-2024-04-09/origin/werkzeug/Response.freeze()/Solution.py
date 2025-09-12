from werkzeug.wrappers import Response
import hashlib

def prepare_response_for_pickle(response):
    # Ensure the response is buffered into a list
    # direct_passthrough is turned off to allow modifications and buffering the data
    response.direct_passthrough = False
    
    # Buffer the response data if not already buffered
    if not response.is_sequence:
        response.response = [response.get_data()]
    
    # Set the Content-Length header based on the response content
    content_length = sum(len(chunk) for chunk in response.response)
    response.headers['Content-Length'] = str(content_length)
    
    # Generate ETag if not already set
    if 'ETag' not in response.headers:
        # Create a hash object
        hash_obj = hashlib.md5()
        # Update hash object with response data
        for chunk in response.response:
            hash_obj.update(chunk)
        # Set the ETag header using the hexdigest of md5 hash
        etag = hash_obj.hexdigest()
        response.set_etag(etag)
    
    return response

# Example usage:
response = Response("Hello, world!")
prepared_response = prepare_response_for_pickle(response)
print(prepared_response.headers)
# Should print headers with Content-Length and ETag
