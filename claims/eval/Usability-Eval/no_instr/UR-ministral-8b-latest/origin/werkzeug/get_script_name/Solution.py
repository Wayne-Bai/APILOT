from werkzeug.wrappers import Request

# Create a dummy request to emulate a WSGI environment.
dummy_request = Request({
    'SCRIPT_NAME': '/myapp/'
})

# Capture the SCRIPT_NAME and properly decode it.
script_name = dummy_request.script_name.decode()

print(script_name)
