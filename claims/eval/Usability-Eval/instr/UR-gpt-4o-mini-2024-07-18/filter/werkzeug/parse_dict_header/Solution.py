from werkzeug.datastructures import MultiDict

def parse_key_value_pairs(input_string):
    """
    Parse a string of key=value pairs and return a dictionary.
    
    The input format should follow the rules described in RFC 2068 Section 2.
    
    :param input_string: A string of key=value pairs separated by commas.
    :return: A dictionary containing the parsed key-value pairs.
    """
    # Split the input string by commas and strip whitespace
    pairs = [pair.strip() for pair in input_string.split(',')]
    
    # Initialize a MultiDict to hold the key-value pairs
    multi_dict = MultiDict()
    
    # Iterate through the pairs and add them to the MultiDict
    for pair in pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
            multi_dict.add(key.strip(), value.strip())

    # Convert MultiDict to a regular dictionary
    result_dict = {key: multi_dict.getlist(key) for key in multi_dict.keys()}
    
    return result_dict

# Example usage:
input_string = "key1=value1, key2=value2, key1=value3"
parsed_dict = parse_key_value_pairs(input_string)
print(parsed_dict)
