from werkzeug.http import parse_dict_header

# sample input
input_string = "key1=value1, key2=value2, key3=value3"

# convert the input string into a dictionary
out_dict = parse_dict_header(input_string)

# print the dictionary
print(out_dict)
