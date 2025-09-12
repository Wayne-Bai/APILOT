# Importing the required libraries
from werkzeug.wrappers import Request, Response
import json

# Define a function to parse the incoming JSON request data
def parse_json_request(environ, start_response):
    """Parses the incoming JSON request data and returns it."""
    
    # Create a Request object
    request = Request(environ)
    
    # Check if the request method is POST and the content type is application/json
    if request.method == 'POST' and request.content_type == 'application/json':
        # Get the JSON data from the request
        data = request.get_json()
        
        # Return the JSON data as a Response object
        return Response(json.dumps(data), mimetype='application/json')(environ, start_response)
    else:
        # Return an error response if the request method or content type is incorrect
        return Response("Invalid request", status=400)(environ, start_response)

# Define a main function to test the parse_json_request function
def main(environ, start_response):
    return parse_json_request(environ, start_response)

# Run the main function
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    with make_server('localhost', 8000, main) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()
