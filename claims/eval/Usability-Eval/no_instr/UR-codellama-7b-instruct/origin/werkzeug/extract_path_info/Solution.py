from werkzeug.urls import url_parse

# URL to be parsed
url = 'https://www.example.com/path/to/resource?query=1'

# Parse the URL and extract the path info
parsed_url = url_parse(url)
path_info = parsed_url.path

print(path_info)  # Output: '/path/to/resource'
