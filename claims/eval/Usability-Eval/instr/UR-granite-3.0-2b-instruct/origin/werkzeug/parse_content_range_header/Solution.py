from werkzeug import _response

def parse_range_header(range_header):
    try:
        start, end = map(int, range_header.split('-')[1].split('/'))
        return _response.ContentRange(start, end)
    except ValueError:
        return None
