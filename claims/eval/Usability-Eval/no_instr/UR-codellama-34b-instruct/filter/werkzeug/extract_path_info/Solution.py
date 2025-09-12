
from werkzeug.urls import url_parse

def get_path_info(url):
    parsed_url = url_parse(url)
    return parsed_url.path, parsed_url.params

# Example usage
url = "http://example.com/path/to/resource?param1=value1&param2=value2"
path_info = get_path_info(url)
print(path_info)  # ('/path/to/resource', {'param1': 'value1', 'param2': 'value2'})
