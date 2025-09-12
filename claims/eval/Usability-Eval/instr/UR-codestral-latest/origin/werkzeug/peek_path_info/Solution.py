from werkzeug.urls import url_parse

def get_next_segment(url):
    parsed_url = url_parse(url)
    path = parsed_url.path
    path_segments = path.strip('/').split('/')
    return path_segments[1] if len(path_segments) > 1 else None

# Test the function
print(get_next_segment('http://example.com/first_segment/second_segment'))  # Outputs: second_segment
print(get_next_segment('http://example.com'))  # Outputs: None
