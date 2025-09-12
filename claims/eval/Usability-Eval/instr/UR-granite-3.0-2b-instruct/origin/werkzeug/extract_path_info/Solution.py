from werkzeug import url_parse

def extract_path_info(url):
    parsed_url = url_parse(url)
    path_info = parsed_url.path_info
    return path_info

# Example usage:
url = "https://example.com/path/to/resource?query=string#fragment"
print(extract_path_info(url))  # Output: /path/to/resource
