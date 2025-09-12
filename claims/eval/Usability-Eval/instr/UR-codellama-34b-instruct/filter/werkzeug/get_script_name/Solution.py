import sys
from werkzeug.wrappers import Request, Response
from werkzeug.urls import url_decode

# Create a new Request object with the current WSGI environment
req = Request(environ)

# Extract the SCRIPT_NAME variable from the request
script_name = req.environ.get('SCRIPT_NAME', '')

# Decode the script name using the urllib module
script_name = url_decode(script_name, 'utf-8')

# Print the decoded script name to the console
print("Decoded script name:", script_name)
