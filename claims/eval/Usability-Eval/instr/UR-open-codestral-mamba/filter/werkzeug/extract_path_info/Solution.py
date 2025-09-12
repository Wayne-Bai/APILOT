from werkzeug.urls import url_parse

def extract_path_info(url):
    parsed_url = url_parse(url)
    path_info = parsed_url.path
    return path_info

# Test the function
url = "https://www.example.com/path/info"
path_info = extract_path_info(url)
print(path_info)
