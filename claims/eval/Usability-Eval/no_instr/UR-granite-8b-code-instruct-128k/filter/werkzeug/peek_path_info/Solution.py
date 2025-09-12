from werkzeug.routing import BaseConverter
import re

class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super(RegexConverter, self).__init__(url_map)
        self.regex = re.compile(regex)

    def to_python(self, value):
        return self.regex.sub('', value)

    def to_url(self, value):
        return value
