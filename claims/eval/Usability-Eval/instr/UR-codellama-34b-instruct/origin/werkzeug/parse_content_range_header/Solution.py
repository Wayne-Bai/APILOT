from werkzeug import wsgi

class ContentRange:
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
    
    def parse(header_value):
        if not header_value:
            return None
        parts = header_value.split('-')
        if len(parts) != 2:
            return None
        start, end = parts[0], parts[1]
        if not start or not end:
            return None
        try:
            start = int(start)
            end = int(end)
        except ValueError:
            return None
        return ContentRange(start, end)
