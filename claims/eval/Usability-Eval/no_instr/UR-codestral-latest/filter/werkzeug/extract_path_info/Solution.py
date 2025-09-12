from werkzeug.wrappers import Request

def extract_path_info(url):
    request = Request({"PATH_INFO": url})
    return request.path

# Let's try it with an example
url = "/some/path/info"
print(extract_path_info(url))  # Should print: /some/path/info
