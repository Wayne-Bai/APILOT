from werkzeug.urls import url_decode

# Define the input list of key-value pairs
input_list = [('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')]

# Use url_decode to convert the input list into a Python dictionary
output_dict = url_decode(input_list)

print(output_dict)
