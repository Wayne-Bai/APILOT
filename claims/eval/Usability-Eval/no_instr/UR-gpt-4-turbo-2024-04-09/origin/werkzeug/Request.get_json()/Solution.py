from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    # Ensure the request is in JSON format
    if request.is_json:
        data = request.get_json()
        return Response(str(data), mimetype='application/json')
    else:
        return Response('Invalid request format', status=400)

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
