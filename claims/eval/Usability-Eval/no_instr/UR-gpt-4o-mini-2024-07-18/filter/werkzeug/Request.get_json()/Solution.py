from werkzeug.wrappers import Request, Response

def app(environ, start_response):
    request = Request(environ)
    if request.method == 'POST' and request.content_type == 'application/json':
        json_data = request.get_json()
        response_data = {'received': json_data}
        response = Response(response_data, content_type='application/json', status=200)
    else:
        response = Response('Invalid request. Please send a JSON payload.', status=400)

    return response(environ, start_response)
