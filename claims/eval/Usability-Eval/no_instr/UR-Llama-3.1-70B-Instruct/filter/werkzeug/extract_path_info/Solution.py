from werkzeug import DispatcherMiddleware, ScriptNameMiddleware
from werkzeug.wrappers import Response
from werkzeug.serving import run_simple

# Sample application for root URL
def simple_app(environ, start_response):
    body = b"Root application"
    return Response(body)(environ, start_response)

# Sample application for admin URL
def admin_app(environ, start_response):
    body = b"Admin application"
    return Response(body)(environ, start_response)

# Sample application for blog URL
def blog_app(environ, start_response):
    body = b"Blog application"
    return Response(body)(environ, start_response)

# Create dispatcher with mounting points
app = DispatcherMiddleware(simple_app, {
    '/admin': admin_app,
    '/blog': blog_app,
    # This is the path info middleware which will be used to extract path info
    '/path': lambda environ, start_response: Response(list(environ['PATH_INFO'].split('/')))(environ, start_response)
})

# Using ScriptNameMiddleware to handle script name 
app = ScriptNameMiddleware(app)

# Running the development server
if __name__ == '__main__':
    run_simple('localhost', 5000, app, use_reloader=True)
