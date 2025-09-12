from werkzeug.http import parse_range_header

def parse_range_header_to_content_range(range_header):
    """
    Parses a range header into a ContentRange object or None if parsing is not possible.

    :param range_header: The range header string to parse.
    :return: A ContentRange object or None if parsing fails.
    """
    try:
        range_spec = parse_range_header(range_header)
        if range_spec is None or not range_spec.ranges:
            return None
        return range_spec
    except ValueError:
        return None
