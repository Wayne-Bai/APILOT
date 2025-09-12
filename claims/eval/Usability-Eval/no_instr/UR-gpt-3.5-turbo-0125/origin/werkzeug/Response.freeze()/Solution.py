
from werkzeug.wrappers.response import Response

class PicklableResponse(Response):
    def make_conditional(self, request):
        response = super(PicklableResponse, self).make_conditional(request)
        if 'ETag' not in response.headers:
            response.set_etag(response.get_etag())
        response.get_data()
        response.freeze()
        response.headers['Content-Length'] = response.content_length
        return response
