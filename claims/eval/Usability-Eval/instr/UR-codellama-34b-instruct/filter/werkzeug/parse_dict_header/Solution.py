from werkzeug import http

# Define the list of key-value pairs
kv_pairs = [
    ('name', 'John Doe'),
    ('age', 30),
    ('city', 'New York')
]

# Use Werkzeug to parse the list and convert it into a dictionary
headers = http.parse_list_header(kv_pairs)
print(headers)  # Output: {'name': 'John Doe', 'age': '30', 'city': 'New York'}
