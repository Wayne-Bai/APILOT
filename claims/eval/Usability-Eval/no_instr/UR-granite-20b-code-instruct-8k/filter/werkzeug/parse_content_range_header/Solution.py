import werkzeug

def parse_range_header(header):
    """
    Parses a range header into a ContentRange object or None if parsing is not possible.
    """
    range_header = werkzeug.http.parse_range_header(header)
    if range_header is None:
        return None
    return werkzeug.http.ContentRange(range_header)
