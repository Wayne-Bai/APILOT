from werkzeug.http import parse_range

def parse_range_header(header):
    """
    Parses a range header into a ContentRange object or None if parsing is not possible.

    :param header: The range header to parse.
    :return: A ContentRange object if parsing is successful, None otherwise.
    """
    try:
        range_header = parse_range(header)
        return range_header
    except ValueError:
        return None
