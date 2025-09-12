from werkzeug.datastructures import MultiDict

def parse_headers(header_lines):
    """
    Parse lists of key, value pairs as described by RFC 2068 Section 2
    and convert them into a python dict.

    :param header_lines: A list of header lines
    :return: A dictionary of parsed headers
    """
    headers = MultiDict()
    for line in header_lines:
        line = line.strip()
        if line:
            key_value = line.split(':', 1)
            if len(key_value) == 2:
                key = key_value[0].strip().lower()
                value = key_value[1].strip()
                headers.add(key, value)
    return dict(headers)

# Example usage
header_lines = [
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language: en-us,en;q=0.5',
    'Accept-Encoding: gzip,deflate',
    'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7',
    'Keep-Alive: 300'
]

headers = parse_headers(header_lines)
print(headers)
