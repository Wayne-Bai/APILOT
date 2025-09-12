from werkzeug import Request

# Assume url is the given URL or the WSGI environment has been passed properly
url = 'http://www.example.com/path/to/resource'

# Create a Request object
request = Request(app=None)

# Extract the path info
path = request.path

print(f"Path Info: {path}")
