from werkzeug.datastructures import Headers

# Create a new headers object
headers = Headers()

# Add a header
headers.add('Content-Type', 'application/json')

# Get a header
content_type = headers.get('Content-Type')

# Print the header
print(content_type)

# Removing a header
headers.remove('Content-Type')

# To display all headers
for key, value in headers.items():
    print(key + ": " + value)
