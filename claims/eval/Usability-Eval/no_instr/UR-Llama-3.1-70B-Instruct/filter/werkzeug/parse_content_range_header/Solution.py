from werkzeug.datastructures import ContentRange

def parse_range_header(range_header):
    """
    Parses a range header into a ContentRange object or None if parsing is not possible.

    :param range_header: The range header string
    :return: ContentRange object or None
    """
    try:
        range_header = range_header.strip()
        if not range_header.startswith('bytes='):
            return None
        range_header = range_header[6:]
        parts = range_header.split('/')
        
        # Validate if the range is syntactically correct
        if len(parts)!= 2:
            return None
        
        range_start, range_end = map(int, parts[0].split('-'))
        if range_end < range_start or range_start < 0:
            return None
        
        size = int(parts[1])
        
        return ContentRange(units='bytes', start=range_start, end=range_end, size=size)
    except ValueError:
        return None


# Example usage:
range_header = "bytes 10-20/40"
content_range = parse_range_header(range_header)

if content_range:
    print("ContentRange: ", content_range)
else:
    print("Parsing failed.")
