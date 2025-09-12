
import tornado.ioloop

def call_callback(callback):
    tornado.ioloop.IOLoop.current().add_callback(callback)
