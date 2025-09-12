from werkzeug.http import parse_range_header

def parse_range(range_header):
    return parse_range_header(range_header)

# Example usage:
range_header = "bytes=0-499"
content_range = parse_range(range_header)
print(content_range)
