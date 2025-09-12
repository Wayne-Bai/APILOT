from werkzeug.http import parse_options_header

def parse_key_value_pairs(header_value):
    """
    Parse lists of key, value pairs as described by RFC 2068 Section 2
    and convert them into a Python dict.

    :param header_value: The header value containing key, value pairs.
    :return: A dictionary with parsed key, value pairs.
    """
    # Use werkzeug's parse_options_header to parse the header value
    parsed_header = parse_options_header(header_value)
    
    # Convert the parsed header into a dictionary
    result_dict = {}
    for key, value in parsed_header[1].items():
        result_dict[key] = value
    
    return result_dict

# Example usage:
header_value = 'key1=value1; key2=value2; key3=value3'
parsed_dict = parse_key_value_pairs(header_value)
print(parsed_dict)
