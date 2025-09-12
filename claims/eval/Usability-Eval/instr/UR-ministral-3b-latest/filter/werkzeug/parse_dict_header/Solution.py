from werkzeug.exceptions import HTTPException, NotFound

def parse_params(params):
    headers = {}
    if isinstance(params, dict):
        return params
    for key, value in params:
        headers[key] = value
    return headers

# Example usage:
params = [("key1", "value1"), ("key2", "value2")]
parsed_params = parse_params(params)
print(parsed_params)  # Output: {'key1': 'value1', 'key2': 'value2'}
