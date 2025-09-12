from werkzeug.datastructures import Headers

# Create a new Headers object
headers = Headers()

# Add a header
headers.add('Content-Type', 'application/json')

# Add another header
headers.add('Authorization', 'Bearer YOUR_TOKEN_HERE')

# Add another header
headers.add('Accept', 'application/json')

# Access the headers
print(headers.to_string())

# Access a single header by key
print(headers.get('Content-Type'))

# Modify an existing header
headers['Authorization'] = 'Bearer NEW_TOKEN_HERE'

# Remove a header
del headers['Accept']

# Access the headers again
print(headers.to_string())
