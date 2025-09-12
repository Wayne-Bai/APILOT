from werkzeug.http import parse_range_header, ContentRange

def parse_range_header(range_header, entity_length):
    range_info = parse_range_header(range_header, entity_length)
    if range_info is None:
        return None
    else:
        start, stop = range_info[0]
        return ContentRange(entity_length, start=start, stop=stop)

# Example usage:
range_header = 'bytes=0-499'
entity_length = 1000
content_range = parse_range_header(range_header, entity_length)
if content_range is not None:
    print(content_range)
else:
    print("Parsing failed")
