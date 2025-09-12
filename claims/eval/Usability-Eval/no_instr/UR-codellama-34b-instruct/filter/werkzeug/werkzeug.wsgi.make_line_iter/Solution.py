import werkzeug.wsgi

# Set up a sample input stream
stream = io.BytesIO(b"Hello, world!")

# Iterate over the input stream in chunks
for chunk in werkzeug.wsgi.chunk_iter(stream, 6):
    print(chunk)
