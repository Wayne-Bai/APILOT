from werkzeug.datastructures import ContentRange

def parse_range_header(header):
    try:
        return ContentRange.from_string(header)
    except ValueError:
        return None
