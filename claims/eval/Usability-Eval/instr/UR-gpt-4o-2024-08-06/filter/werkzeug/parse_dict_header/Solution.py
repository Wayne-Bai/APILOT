from werkzeug.http import parse_dict_header

def parse_key_value_pairs(header_string):
    """
    Parse a list of key, value pairs from a given header string as described by RFC 2068 Section 2
    and convert them into a dictionary.

    :param header_string: The header string containing key, value pairs.
    :return: A dictionary containing parsed key, value pairs.
    """
    return parse_dict_header(header_string)

# Example usage:
header_string = 'key1="value1"; key2="value2"'
parsed_dict = parse_key_value_pairs(header_string)
print(parsed_dict)  # Output: {'key1': 'value1', 'key2': 'value2'}
