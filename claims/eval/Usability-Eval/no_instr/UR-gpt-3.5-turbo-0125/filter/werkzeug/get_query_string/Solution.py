
from urllib.parse import parse_qs

def get_query_string(environ):
    query_string = environ.get('QUERY_STRING', '')
    if query_string:
        return parse_qs(query_string)
    else:
        return {}

# Example usage
environ = {'QUERY_STRING': 'name=John&age=30'}
query_params = get_query_string(environ)
print(query_params)
