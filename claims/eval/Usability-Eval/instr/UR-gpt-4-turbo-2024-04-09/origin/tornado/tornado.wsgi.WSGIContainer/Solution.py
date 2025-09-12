import tornado.wsgi
import tornado.httpserver
import tornado.ioloop
from flask import Flask

# Create a simple Flask WSGI application
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Flask!'

# Create a WSGI container with the Flask application
wsgi_container = tornado.wsgi.WSGIContainer(app)

# Create a Tornado HTTP server which can serve the WSGI container
http_server = tornado.httpserver.HTTPServer(wsgi_container)

# Bind the HTTP server to localhost on port 8000
http_server.listen(8000)

# Start the I/O loop
if __name__ == "__main__":
    tornado.ioloop.IOLoop.instance().start()
