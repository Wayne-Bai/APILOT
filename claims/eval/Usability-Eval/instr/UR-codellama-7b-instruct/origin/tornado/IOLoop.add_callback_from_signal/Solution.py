
import tornado

def next_io_loop(callback):
    tornado.ioloop.IOLoop.instance().add_callback(callback)
