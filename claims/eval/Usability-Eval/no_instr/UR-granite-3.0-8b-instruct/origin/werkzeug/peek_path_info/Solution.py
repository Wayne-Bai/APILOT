from werkzeug.routing import BaseConverter

class NextSegmentConverter(BaseConverter):
    def __init__(self):
        super().__init__()

    def to_python(self, value):
        return value.split('/')[-1] if value else None

    def to_url(self, value):
        return f'/{value}/' if value else ''
