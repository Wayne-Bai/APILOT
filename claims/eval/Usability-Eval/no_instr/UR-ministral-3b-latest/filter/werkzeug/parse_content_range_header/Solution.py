from werkzeug.http import parse_range

def parse_content_range(header):
    try:
        return parse_range(header).content_range
    except ValueError:
        return None
