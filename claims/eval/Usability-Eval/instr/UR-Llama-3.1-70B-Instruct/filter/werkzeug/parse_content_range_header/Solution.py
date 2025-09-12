from werkzeug.datastructures import ContentRange

def parse_range_header(header):
    """
    Parses a range header into a ContentRange object or None if parsing is not possible.

    :param header: The range header to parse
    :return: A ContentRange object or None
    """
    if not header:
        return None

    parts = header.split("=")
    if len(parts)!= 2 or parts[0].strip().lower()!= "bytes":
        return None

    units, range_set = parts
    ranges = range_set.split(",")

    parsed_ranges = []
    for r in ranges:
        start, end = r.split("-")
        try:
            start = int(start)
            end = int(end)
        except ValueError:
            return None

        # Check for invalid ranges
        if start > end:
            return None

        parsed_ranges.append((start, end))

    return ContentRange(units, None, parsed_ranges, None)

# Example usage:
header = "bytes=0-10, 20-30"
content_range = parse_range_header(header)
if content_range is not None:
    print(content_range.units)
    print(content_range.ranges)
else:
    print("Failed to parse range header")
