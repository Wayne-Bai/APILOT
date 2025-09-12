from werkzeug.datastructures import MultiDict

def parse_key_value_pairs(kv_pairs):
    """
    Parse a list of key, value pairs as described by RFC 2068 Section 2 
    and convert them into a Python dictionary.

    Args:
        kv_pairs (list): List of key-value strings (e.g., ["key1=value1", "key2=value2"]).

    Returns:
        dict: A dictionary with the parsed key-value pairs.
    """
    data_dict = MultiDict()
    for pair in kv_pairs:
        if '=' in pair:
            key, value = pair.split('=', 1)
            data_dict.add(key.strip(), value.strip())
    
    return dict(data_dict)

# Example usage
kv_pairs = ["key1=value1", "key2=value2", "key3=value3"]
result = parse_key_value_pairs(kv_pairs)
print(result)
