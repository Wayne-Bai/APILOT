from werkzeug.wrappers import Request, Response
import json

@Request.application
def application(request):
    # Check if the request has JSON data
    if request.is_json:
        # Parse the JSON data
        data = request.get_json()
        if data is None:
            response = Response("Invalid or missing JSON data", mimetype='text/plain', status=400)
        else:
            # Return the JSON data
            response = Response(json.dumps(data), mimetype='application/json', status=200)
    else:
        response = Response("Request content type is not application/json", mimetype='text/plain', status=400)
    
    return response

# To run the app with a WSGI server like werkzeug's testing server, you would add something like:
# if __name__ == '__main__':
#     from werkzeug.serving import run_simple
#     run_simple('localhost', 5000, application)
