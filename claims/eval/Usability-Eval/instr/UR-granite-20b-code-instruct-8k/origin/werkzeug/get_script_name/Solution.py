from werkzeug.routing import BaseConverter

class ScriptNameConverter(BaseConverter):
    def to_python(self, value):
        return value.decode('utf-8')

    def to_url(self, value):
        return value.encode('utf-8')
