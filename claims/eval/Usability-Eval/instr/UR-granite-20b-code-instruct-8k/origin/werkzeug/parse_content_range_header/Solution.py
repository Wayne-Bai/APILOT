from werkzeug.http import parse_content_range

def parse_range_header(header):
    try:
        return parse_content_range(header)
    except ValueError:
        return None
