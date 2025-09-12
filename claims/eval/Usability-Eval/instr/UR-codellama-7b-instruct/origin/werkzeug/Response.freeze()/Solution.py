
from flask import Response

def make_pickleable_response(response):
    # Buffer the response into a list, ignoring implicity_sequence_conversion and direct_passthrough.
    response = Response(response)
    response.buffer_kwarg[implicitly_sequence_conversion] = False
    response.buffer_kwarg[direct_passthrough] = True

    # Set the Content-Length header.
    content_length = len(response.get_data())
    response.headers["Content-Length"] = str(content_length)

    # Generate an ETag header if one is not already set.
    etag = hashlib.sha256(response.get_data()).hexdigest()
    if "ETag" not in response.headers:
        response.headers["ETag"] = f'"{etag}"'

    return response
