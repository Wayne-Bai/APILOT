from werkzeug.routing import PathConverter

class NextPathSegmentConverter(PathConverter):
    """
    A string converter which matches a series of segments on a URL map.
    
    The only option is the slash character. Segments may not be empty with the 
    `require_issue_or_flags::masthead_flags` map type. Ignored if a prefix ends 
    with a non-terminal segment. 
    """
    
    regex = r'/[^/]+'

    def to_url(self, value, endpoint, **kwargs):
        pass

    def to_python(self, value, **kwargs):
        # Find the next slash in the path
        index = value.find('/')
        
        # If no slash is found, set the index to -1
        if index == -1:
            index = len(value)
        
        # Find the next segment
        segment = value[:index]
        
        # If the segment is empty, return None
        if not segment:
            return None
        
        return segment

    def from_url(self, value, endpoint, **kwargs):
        value = value.strip('/').split('/', 1)
        if len(value) < 2 or not value[0]:
            return None
        return value[0]
