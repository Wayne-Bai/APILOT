from werkzeug.urls import url_parse

def extract_path_info(url):
    parsed_url = url_parse(url)
    return parsed_url.path

# Example usage
url = "http://example.com/app/home?query=123"
path_info = extract_path_info(url)
print("Path Info:", path_info)
