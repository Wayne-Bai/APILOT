from werkzeug.urls import url_parse

def extract_path(url):
    parsed_url = url_parse(url)
    return parsed_url.path

url = "http://example.com/some/path"
print(extract_path(url))  # Output: '/some/path'
