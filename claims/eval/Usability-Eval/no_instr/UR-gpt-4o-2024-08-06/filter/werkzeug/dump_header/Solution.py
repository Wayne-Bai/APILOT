from werkzeug.datastructures import Headers

# Create a Headers object
headers = Headers()

# Add some headers
headers.add('Content-Type', 'text/html')
headers.add('Cache-Control', 'no-cache')
headers.add('Custom-Header', 'value')

# Dump (serialize) the headers to a string
dumped_headers = headers.to_wsgi_list()

# Print the dumped headers
for header in dumped_headers:
    print(f"{header[0]}: {header[1]}")
