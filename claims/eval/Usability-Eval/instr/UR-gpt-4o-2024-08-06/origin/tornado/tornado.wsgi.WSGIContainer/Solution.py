import tornado.ioloop
import tornado.httpserver
from tornado.wsgi import WSGIApplication
from flask import Flask

# Define your WSGI application using a framework like Flask
flask_app = Flask(__name__)

@flask_app.route("/")
def index():
    return "Hello from Flask running on Tornado!"

# Wrap the Flask application with Tornado's WSGIContainer
tornado_app = WSGIApplication([
    (r".*", tornado.web.FallbackHandler, dict(fallback=flask_app)),
])

def main():
    # Create a Tornado HTTP server and bind it to the specified port
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(8000)  # You can choose any suitable port

    # Start the Tornado I/O loop
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
