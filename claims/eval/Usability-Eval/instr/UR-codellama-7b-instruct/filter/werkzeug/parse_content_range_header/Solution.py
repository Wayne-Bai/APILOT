import werkzeug

def parse_range_header(header):
    try:
        parsed_range = werkzeug.ContentRange(header)
        return parsed_range
    except ValueError:
        return None