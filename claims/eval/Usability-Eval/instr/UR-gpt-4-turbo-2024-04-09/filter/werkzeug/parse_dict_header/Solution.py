from werkzeug.http import parse_dict_header

def parse_header(header_string):
    # Parse the header string according to RFC 2068 Section 2
    parsed_dict = parse_dict_header(header_string)
    return parsed_dict

# Example usage
header_str = 'type="text/plain"; charset="utf-8"'
parsed_header = parse_header(header_str)
print(parsed_header)
