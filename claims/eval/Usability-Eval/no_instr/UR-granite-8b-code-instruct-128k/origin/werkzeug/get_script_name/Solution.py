from werkzeug.utils import script_name

def my_app(environ, start_response):
    script_name = environ.get('SCRIPT_NAME', '')
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello, World!']

def my_wrapper(app):
    def inner(environ, start_response):
        script_name = environ.get('SCRIPT_NAME', '')
        return app(environ, start_response)
    return inner

application = my_wrapper(my_app)
