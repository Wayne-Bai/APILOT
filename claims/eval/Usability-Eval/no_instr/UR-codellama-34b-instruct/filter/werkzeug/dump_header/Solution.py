import werkzeug.wrappers as wkz

# Create a new request object
request = wkz.Request()

# Dump the headers of the request
print(request.headers)
