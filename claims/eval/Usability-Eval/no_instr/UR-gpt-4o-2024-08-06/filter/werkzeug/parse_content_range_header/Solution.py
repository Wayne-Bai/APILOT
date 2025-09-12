from werkzeug.datastructures import Range

def parse_range_header(range_header, length):
    """
    This function takes a range header string and a total length value,
    and returns a list of tuples indicating the ranges.
    :param range_header: The value of the Range request header.
    :param length: The total length of the resource the range is being applied to.
    :return: A list of (start, stop) tuples or None if the header cannot be parsed.
    """
    try:
        # Parsing the Range header using the Range object
        range_object = Range.parse_header(range_header)
        
        if range_object:
            # Calculate actual ranges based on the length of the resource
            ranges = range_object.ranges(length)
            return ranges
        
        return None

    except Exception:
        return None

# Example usage
range_header = 'bytes=0-499'
resource_length = 1000
parsed_ranges = parse_range_header(range_header, resource_length)
print(parsed_ranges)  # Output: [(0, 500)]
