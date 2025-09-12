
import werkzeug

def parse_range(header):
    try:
        # Parse the range header using the Werkzeug parser
        return werkzeug.http.parse_content_range(header)
    except ValueError:
        # If parsing fails, return None
        return None
