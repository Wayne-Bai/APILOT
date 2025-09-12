from werkzeug.datastructures import Headers

# Create a sample HTTP headers
sample_headers = Headers([
    ('Content-Type', 'application/json'),
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
])

# Dump the HTTP headers
for key, value in sample_headers:
    print(f'{key}: {value}')
