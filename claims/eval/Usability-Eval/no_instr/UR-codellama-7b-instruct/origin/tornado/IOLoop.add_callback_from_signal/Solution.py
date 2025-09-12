
import tornado.ioloop

def execute_on_next_iteration(callback):
    tornado.ioloop.IOLoop.current().add_callback(callback)
