from werkzeug.http import parse_dict_header
header = 'key1=value1; key2=value2; key3=value3'
dict_header = parse_dict_header(header)
print(dict_header)
