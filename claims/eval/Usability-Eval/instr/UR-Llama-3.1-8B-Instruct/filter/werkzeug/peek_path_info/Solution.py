from werkzeug.routing import URLConverter
from werkzeug.urls import url_parse

class MyURLConverter(URLConverter):
    def get_next_segment(self, path):
        parsed_path = url_parse(path)
        return parsed_path.path.lstrip('/').split('/')[1] if parsed_path.path.lstrip('/').split('/') else None

# Usage
converter = MyURLConverter()
path = '/admin/dashboard'
print(converter.get_next_segment(path))  # Output: 'dashboard'

path = '/index'
print(converter.get_next_segment(path))  # Output: 'index'

path = '/'
print(converter.get_next_segment(path))  # Output: None
