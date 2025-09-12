from werkzeug.http import parse_range

def parse_range_header(header):
    range_obj = parse_range(header)
    if range_obj:
        return range_obj
    else:
        return None
