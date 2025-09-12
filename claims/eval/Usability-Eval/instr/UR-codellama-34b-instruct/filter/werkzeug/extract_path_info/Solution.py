
from werkzeug import urls

url = "https://example.com/path/to/resource?query=string"
path_info = urls.parse(url)["path"]
print(path_info)  # Outputs "/path/to/resource"
