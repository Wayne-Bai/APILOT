from werkzeug.http import parse_range_header, parse_content_range_header

def parse_range_header_to_content_range(range_header):
    if range_header is None:
        return None

    range_data = parse_range_header(range_header)
    if range_data:
        return {
            'unit': range_data.unit,
            'ranges': range_data.ranges
        }
    return None

# Example usage
range_header = "bytes=0-10"
content_range = parse_range_header_to_content_range(range_header)
print(content_range)
