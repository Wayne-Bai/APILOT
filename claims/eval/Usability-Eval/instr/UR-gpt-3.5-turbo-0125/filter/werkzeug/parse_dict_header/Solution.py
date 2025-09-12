
from werkzeug.datastructures import parse_dict_header

# Example header string to parse
header_string = 'key1=value1, key2=value2, key3=value3'

# Parse the header string into a Python dict
parsed_dict = {}
for key, value in parse_dict_header(header_string).items():
    parsed_dict[key] = value

print(parsed_dict)
