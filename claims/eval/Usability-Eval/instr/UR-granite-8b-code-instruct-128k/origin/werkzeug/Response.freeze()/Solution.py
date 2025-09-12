from werkzeug.wsgi import SharedDataMiddleware

def make_response_ready_to_be_pickled(response):
    response_list = []
    response_list.append(response)

    if not response.direct_passthrough and not response.implicit_sequence_conversion:
        response_list.extend(response)

    if 'Content-Length' not in response.headers:
        response.headers['Content-Length'] = str(len(response_list))

    if 'ETag' not in response.headers:
        response.headers['ETag'] = generate_etag(response_list)

    return response_list