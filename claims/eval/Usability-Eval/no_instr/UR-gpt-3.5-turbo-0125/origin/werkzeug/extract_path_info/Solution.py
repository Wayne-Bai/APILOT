
# Importing the necessary module from werkzeug
from werkzeug.urls import url_parse

# Function to extract path info from the given URL
def extract_path_info(url):
    parsed_url = url_parse(url)
    path_info = parsed_url.path
    return path_info

# Example usage
url = "http://www.example.com/path/to/resource"
path_info = extract_path_info(url)
print(path_info)
