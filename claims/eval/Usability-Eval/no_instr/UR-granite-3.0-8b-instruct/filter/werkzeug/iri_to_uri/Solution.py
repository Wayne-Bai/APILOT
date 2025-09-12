from werkzeug.routing import BaseConverter

class IRItoURIConverter(BaseConverter):
    def to_python(self, value):
        return self.to_uri(value)

    def to_uri(self, value):
        return value.replace('%2F', '/').replace('%3A', ':').replace('%3F', '?').replace('%23', '#').replace('%40', '@').replace('%5E', '^').replace('%27', "'").replace('%28', '(').replace('%29', ')').replace('%2C', ',').replace('%3B', ';').replace('%3D', '=').replace('%2B', '+').replace('%24', '$').replace('%5B', '[').replace('%5D', ']').replace('%22', '"').replace('%3E', '>').replace('%3C', '<').replace('%7E', '~')

# Usage
converter = IRItoURIConverter()
uri = converter.to_python('http%3A%2F%2Fexample.com%2Fpath%2F%3Fq%3Dvalue')
print(uri)  # Output: http://example.com/path?q=value
