from werkzeug.wrappers import Response
import hashlib
import io

def prepare_response(data):
    # Buffer the response into a list
    buf = io.BytesIO()
    for chunk in data:
        buf.write(chunk)
    response_data = buf.getvalue()

    # Create a Response object
    response = Response(response_data)

    # Set the Content-Length header
    response.headers['Content-Length'] = len(response_data)

    # Generate an ETag header if one is not already set
    if 'ETag' not in response.headers:
        etag = hashlib.md5(response_data).hexdigest()
        response.headers['ETag'] = etag

    return response
