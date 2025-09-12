from werkzeug.datastructures import ContentRange
def parse_range_header(range_header):
    """Parse a range header into a ContentRange object or None if parsing is not possible."""
    if not range_header:
        return None
    try:
        return ContentRange.parse(range_header)
    except ValueError:
        return None
