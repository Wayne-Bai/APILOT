import tornado.ioloop

def call_callback_on_next_iteration(callback):
    tornado.ioloop.IOLoop.current().add_callback(callback)
