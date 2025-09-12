import tornado.ioloop

# Makes this the IOLoop for the current thread.
current_ioloop = tornado.ioloop.IOLoop.current()
