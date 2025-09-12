
from werkzeug.wrappers import Request, Response

def handle_request(req):
    # Create a line-based iterator from the request body
    lines = req.iter_lines()
    
    # Iterate over each line and print it to stdout
    for line in lines:
        print(line)
        
# Define a route that accepts requests and handles them with handle_request
@app.route('/', methods=['POST'])
def handle_post():
    req = request.get_data()
    return Response(handle_request(req), mimetype='text/plain')
