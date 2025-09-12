
from werkzeug.datastructures import Range
from werkzeug.http import parse_range_header

def parse_range_header_to_content_range(header):
    ranges = parse_range_header(header)
    
    if ranges:
        content_range = Range.to_content_range(ranges[0])
        return content_range
    else:
        return None
