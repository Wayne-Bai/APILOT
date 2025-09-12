from werkzeug.http import parse_range_header

def parse_content_range_header(header_value):
    """
    Parse the Range header value into a ContentRange object or None.

    Args:
    header_value (str): The value of the Range header.

    Returns:
    werkzeug.datastructures.ContentRange: The parsed ContentRange object or None if parsing fails.
    """
    return parse_range_header(header_value)

# Example usage
header = "bytes=200-1000"
parsed_range = parse_content_range_header(header)
print(parsed_range)
