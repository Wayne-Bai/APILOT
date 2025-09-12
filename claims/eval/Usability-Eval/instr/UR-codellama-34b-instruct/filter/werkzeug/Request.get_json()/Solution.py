from werkzeug import JSONRequest
from werkzeug.wrappers import Request

# Define a function that parses the incoming JSON request data
def parse_json(request):
    # Create a new JSONRequest object from the incoming request
    json_request = JSONRequest(request)
    
    # Parse the JSON data and return it as a dictionary
    json_data = json_request.get_json()
    return json_data

# Use the function to parse the incoming request data
@app.route('/', methods=['POST'])
def index():
    # Get the incoming request data
    request = Request(environ)
    
    # Parse the JSON data and store it in a variable
    data = parse_json(request)
    
    # Do something with the parsed data here
    print(data)
