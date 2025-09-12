from werkzeug.datastructures import Headers

# define a headers object
headers = Headers()
headers.add('Content-Type', 'application/json')

# add a new header if it does not already exist
if 'User-Agent' not in headers:
    headers.add('User-Agent', 'MyApp/1.0')

# if header already exists, modify it
headers.set('Content-Type', 'application/xml')

print(dict(headers))
