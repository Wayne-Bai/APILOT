from werkzeug.utils import secure_filename, dumps

def make_response_picklable(response):
    # Buffer the response into a list, ignoring implicitly_sequence_conversion and direct_passthrough
    response_list = list(response)

    # Set the Content-Length header
    response.headers['Content-Length'] = len(dumps(response_list))

    # Generate an ETag header if one is not already set
    if 'ETag' not in response.headers:
        response.headers['ETag'] = f"W/{int(response.status_code)}"

    return response
