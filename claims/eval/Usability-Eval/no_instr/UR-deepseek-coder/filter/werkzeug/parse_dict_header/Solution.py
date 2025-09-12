from werkzeug.http import parse_list_header

def parse_key_value_pairs(header_value):
    # Parse the header value into a list of key-value pairs
    parsed_list = parse_list_header(header_value)
    
    # Convert the list of key-value pairs into a dictionary
    result_dict = {}
    for item in parsed_list:
        key, value = item.split('=', 1)
        result_dict[key] = value
    
    return result_dict

# Example usage:
header_value = 'key1=value1; key2=value2; key3=value3'
parsed_dict = parse_key_value_pairs(header_value)
print(parsed_dict)
