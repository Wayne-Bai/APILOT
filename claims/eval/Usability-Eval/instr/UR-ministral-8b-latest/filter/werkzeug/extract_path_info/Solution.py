from werkzeug.utils import secure_filename
from urllib.parse import urlparse

def extract_path_info(url):
    parsed_url = urlparse(url)
    path_info = parsed_url.path
    return path_info

# Example usage:
url = "http://example.com/path/to/resource"
print(extract_path_info(url))
