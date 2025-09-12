from werkzeug.routing import Map, Rule

def get_next_segment(path_info):
    # Split the path_info by '/' and filter out empty segments
    segments = list(filter(None, path_info.split('/')))
    
    # Return the next segment or None if there are no segments left
    return segments[0] if segments else None

# Example usage
path_info = "/foo/bar/baz"
next_segment = get_next_segment(path_info)
print(next_segment)  # Output: 'foo'
