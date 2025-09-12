from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    # Parse the incoming JSON data
    data = request.get_json()
    # Return the parsed data as a JSON response
    return Response(response=str(data), content_type='application/json')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
