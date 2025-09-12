from werkzeug.wrappers import Response

def prepare_response(response):
    # Buffer the response into a list
    response.data = response.get_data(as_text=False, cache_safe=False)

    # Set the Content-Length header
    response.headers['Content-Length'] = len(response.data)

    # Generate an ETag header if one is not already set
    if 'ETag' not in response.headers:
        response.headers['ETag'] = '"%s"' % response.data.decode('utf-8')

    return response
