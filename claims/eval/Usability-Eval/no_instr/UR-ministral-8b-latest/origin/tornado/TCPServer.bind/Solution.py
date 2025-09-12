import tornado.ioloop
import tornado.web
import tornado.netutils
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    address = os.getenv('TORNADO_ADDRESS', '0.0.0.0')
    port = int(os.getenv('TORNADO_PORT', '8888'))

    app = make_app()
    app.listen(port, address=address)
    print(f"Server is listening on {address}:{port}")

    # Keep the main thread alive
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("\nShutting down...")

