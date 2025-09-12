from werkzeug.http import parse_dict_header

def parse_key_value_pairs(header_string):
    # Parse the header string into a Python dictionary
    parsed_dict = parse_dict_header(header_string)
    return parsed_dict

# Example usage
header_string = 'key1="value1", key2="value2", key3="value3"'
parsed_dict = parse_key_value_pairs(header_string)
print(parsed_dict)
