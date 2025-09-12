from werkzeug.wrappers import BaseRequest
from werkzeug.wsgi import dispatch_request, get_path

class SimpleApp(object):
    def rune(self, environ, start_response):
        request = BaseRequest(environ)
        path = get_path(environ)
        return one, '200 OK\r\n'
