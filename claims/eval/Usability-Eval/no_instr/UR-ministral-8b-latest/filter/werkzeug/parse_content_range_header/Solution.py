from werkzeug.http import parse_range

class ContentRange:
    def __init__(self, start, end, total):
        self.start = int(start)
        self.end = int(end)
        self.total = int(total)

def parse_range_header(header):
    try:
        start, end, total = parse_range(header)
        return ContentRange(start, end, total)
    except ValueError:
        return None

# Example usage:
header = "bytes 0-15/100"
parsed_range = parse_range_header(header)
if parsed_range:
    print(f"Start: {parsed_range.start}, End: {parsed_range.end}, Total: {parsed_range.total}")
else:
    print("Failed to parse range header.")
