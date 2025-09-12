from werkzeug import Headers

# Create a new HTTP header
header = Headers()

# Add a header
header.add('Content-Type', 'application/json')

# Print the header
print(header)
