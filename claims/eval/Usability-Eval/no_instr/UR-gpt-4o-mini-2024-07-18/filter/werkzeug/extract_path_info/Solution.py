from werkzeug.urls import url_parse
from werkzeug.wrappers import Request

def extract_path_info(url):
    parsed_url = url_parse(url)
    return parsed_url.path

# Example usage
url = 'http://example.com/some/path?query=param'
path_info = extract_path_info(url)
print(path_info)  # Output: /some/path
