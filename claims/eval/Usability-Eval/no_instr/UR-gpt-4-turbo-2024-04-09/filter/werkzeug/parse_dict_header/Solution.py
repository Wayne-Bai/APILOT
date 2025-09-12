from werkzeug.datastructures import MultiDict

def parse_key_value_pairs(input_string):
    # Werkzeug handles multiple values for the same key using MultiDict
    multi_dict = MultiDict()

    # Splitting the input string by commas to get individual key-value pairs
    pairs = input_string.split(',')
    for pair in pairs:
        # Further split each pair by the equal sign to separate key and value
        key_value = pair.split('=')
        if len(key_value) == 2:
            key, value = key_value
            multi_dict.add(key.strip(), value.strip())

    # Converting MultiDict to a regular dictionary for easier usage in Python
    # (taking the last added value if multiple values exist for the same key)
    regular_dict = multi_dict.to_dict(flat=True)
    return regular_dict

# Example usage
input_string = "key1=value1, key2=value2, key3=value3"
parsed_dict = parse_key_value_pairs(input_string)
print(parsed_dict)
