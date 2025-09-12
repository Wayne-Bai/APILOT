
from werkzeug.http import ContentRange

def parse_range_header(header):
    try:
        return ContentRange(header)
    except ValueError:
        return None
