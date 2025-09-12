from werkzeug.wrappers import Request
from werkzeug.routing import Map, Rule

def create_application(handler):
    def application(environ, start_response):
        request = Request(environ)
        adapter = url_map.bind_to_environ(request.environ)
        handler_args = adapter.match()
        response = handler(**handler_args)
        return response(environ, start_response)
    return application

url_map = Map([Rule('/<arg1>/<arg2>', endpoint='my_handler')])

def my_handler(arg1, arg2):
    args = {'arg1': arg1, 'arg2': arg2}
    return args

application = create_application(my_handler)
