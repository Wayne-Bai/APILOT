from werkzeug.wrappers import Request, Response
import json

# Create a simple WSGI application
def application(environ, start_response):
    # Create a request object
    request = Request(environ)
    
    # Check if the request method is POST and the content type is application/json
    if request.method == 'POST' and request.mimetype == 'application/json':
        # Get the JSON data from the request
        data = request.get_json()
        
        # Return the JSON data as a response
        response = Response(json.dumps(data), mimetype='application/json')
        return response(environ, start_response)
    else:
        # Return an error response if the request method or content type is not supported
        response = Response('Only POST requests with JSON data are supported.', status=400)
        return response(environ, start_response)

# Run the application
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application, use_reloader=True)
