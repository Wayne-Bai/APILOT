from werkzeug.routing import BaseConverter

class NextSegmentConverter(BaseConverter):
    def __init__(self, map, *args, **kwargs):
        super(NextSegmentConverter, self).__init__(map, *args, **kwargs)

    def to_python(self, value):
        if not value:
            return None
        return value.split('/')[-1]

    def to_url(self, value):
        return '/' + '/' .join(value.split('/')[:-1])
