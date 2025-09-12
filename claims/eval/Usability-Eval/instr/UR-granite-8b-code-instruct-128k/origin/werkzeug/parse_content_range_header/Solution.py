from werkzeug.datastructures import Range

def parse_range_header(header):
    try:
        range = Range.from_string(header)
        return range
    except ValueError:
        return None
