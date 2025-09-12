from werkzeug.datastructures import parse_dict_header

def parse_header_pairs(header_string):
    """
    Parse lists of key, value pairs as described by RFC 2068 Section 2 
    and convert them into a python dict.
    
    Args:
        header_string (str): A string containing key, value pairs.

    Returns:
        dict: A dictionary representation of the key, value pairs.
    """
    # Parse the header string into a dictionary
    parsed_dict = parse_dict_header(header_string)
    
    return parsed_dict

# Example usage
header_string = "key1=value1, key2=value2"
print(parse_header_pairs(header_string))
