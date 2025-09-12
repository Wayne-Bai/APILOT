from werkzeug.urls import url_parse

# Sample URL for demonstration
url = 'http://example.com/path/segment'

# Parse the URL
parsed_url = url_parse(url)

# Extract the next path segment
next_segment = None

path_segments = parsed_url.path.split('/')
if len(path_segments) > 1:
    next_segment = path_segments[1]

next_segment
