from werkzeug.wrappers import Request, Response

def application(environ, start_response):
    request = Request(environ)
    
    if request.is_json:
        data = request.get_json()
        response_data = {
            'received': data
        }
        response = Response(response=data, status=200, mimetype='application/json')
    else:
        response = Response(response='No JSON data received', status=400)

    return response(environ, start_response)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
