from werkzeug.http import parse_range_header

class ContentRange:
    def __init__(self, start, end, total):
        self.start = start
        self.end = end
        self.total = total

    def __repr__(self):
        return f"ContentRange(start={self.start}, end={self.end}, total={self.total})"

def parse_content_range_header(header):
    range_header = parse_range_header(header)
    if range_header:
        for range_item in range_header.ranges:
            return ContentRange(range_item.start, range_item.end, range_item.length)
    return None

# Example usage
header = 'bytes=0-499'
content_range = parse_content_range_header(header)
print(content_range)  # Output: ContentRange(start=0, end=499, total=None)
