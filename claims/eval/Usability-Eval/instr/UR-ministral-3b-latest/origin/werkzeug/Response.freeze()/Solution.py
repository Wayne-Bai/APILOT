from werkzeug import Response, ContentType

class CustomBufferedResponse(Response):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def buffer(self):
        return super().buffer()

    def set_content_length(self):
        self.content_length = len(self.data)

    def generate_etag(self):
        if not hasattr(self, 'content_type'):
            self.content_type = ContentType()

        if not hasattr(self, '_etag'):
            self._etag = self._generate_etag()
        return self._etag

    def _generate_etag(self):
        etag_value = self.content_length
        return etag_value

    def to_json(self):
        response = self.data
        response["Content-Length"] = self.content_length
        return response

# Usage

data = b'{"action": "get", "id": 1}'
xml_header = b'<?xml version="1.0"?>\n'
buffered_response = CustomBufferedResponse(data)
buffered_response.set_content_length()
buffered_response.generate_etag()
response_data = buffered_response.to_json()

print(response_data)
