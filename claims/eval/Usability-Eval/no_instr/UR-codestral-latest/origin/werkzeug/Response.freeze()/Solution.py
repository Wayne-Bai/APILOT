from werkzeug.wrappers import Response
import hashlib

def create_response(data):
    # Buffer the response into a list
    buffered_data = list(data)

    response = Response(buffered_data)

    # Set the Content-Length header
    response.headers['Content-Length'] = str(len(buffered_data))

    # Generate an ETag header. Hash the response data to create an ETag
    hash_obj = hashlib.md5(''.join(buffered_data).encode('utf-8'))
    etag = hash_obj.hexdigest()

    if 'ETag' not in response.headers:
        response.headers['ETag'] = etag

    return response
