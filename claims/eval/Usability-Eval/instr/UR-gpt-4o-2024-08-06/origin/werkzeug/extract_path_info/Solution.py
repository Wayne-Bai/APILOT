from urllib.parse import urlparse, unquote
from werkzeug.wrappers import Request

def extract_path_info(url, base_path='/'):
    # Parse the URL to get the path
    parsed_url = urlparse(url)
    # Decode the path and remove the base path portion
    path_info = unquote(parsed_url.path)
    if path_info.startswith(base_path):
        path_info = path_info[len(base_path):]
    return path_info

# Example usage
url = "http://example.com/base/path/info"
base_path = "/base"
path_info = extract_path_info(url, base_path=base_path)
print("Extracted Path Info:", path_info)

# WSGI environment modification
def path_info_from_environ(environ, base_path='/'):
    request = Request(environ)
    path_info = request.path
    if path_info.startswith(base_path):
        path_info = path_info[len(base_path):]
    return path_info
