from urllib.parse import parse_qs

def parse_rfc2068(s):
    # parse_qs returns a dictionary where the keys are the unique keys and the values are lists of values
    # After parsing, we'll convert these lists into single values if they only have one item
    parsed_dict = parse_qs(s)
    return {k: v[0] if len(v) == 1 else v for k, v in parsed_dict.items()}

# example usage
s = "key1=value1&key2=value2&key2=value3"
print(parse_rfc2068(s))  # outputs: {'key1': 'value1', 'key2': ['value2', 'value3']}
