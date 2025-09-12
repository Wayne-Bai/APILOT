from werkzeug.wrappers import Response

class PicklableResponse(Response):
    def make_picklable(self):
        # Buffer the response into a list
        self.response = list(self.response)

        # Set the Content-Length header
        self.content_length = sum(len(chunk) for chunk in self.response)

        # Generate an ETag header if one is not already set
        if 'ETag' not in self.headers:
            import hashlib
            etag = hashlib.md5(self.response[0].encode() if self.response else b'').hexdigest()
            self.set_etag(etag)
