from werkzeug.http import parse_range_header

def parse_content_range(header_value):
    content_range = parse_range_header(header_value)
    return content_range

# Example usage:
range_header = 'bytes=0-499'
parsed_range = parse_content_range(range_header)
print(parsed_range)
