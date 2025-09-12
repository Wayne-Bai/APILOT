import tornado.ioloop
import tornado.web
from tornado.netutil import bind_sockets

def bind_address_and_port(address="127.0.0.1", port=8888):
    # Create a network socket and bind it to the given address and port
    sockets = bind_sockets(port, address=address)
    return sockets[0].getsockname()

def bind_this_server(address="127.0.0.1", port=8888):
    ip_address, server_port = bind_address_and_port(address, port)
    print(f"Server is listening on {ip_address}:{server_port}")
    tornado.ioloop.IOLoop.current().start()

# Application setup
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World!")

if __name__ == "__main__":
    # Application initialization
    app = tornado.web.Application([
        (r"/", MainHandler),
    ])

    # Setting up the server's address and port
    bind_this_server()
