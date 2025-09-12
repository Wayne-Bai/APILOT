import tornado.ioloop

# Clear the IOLoop for the current thread
io_loop = tornado.ioloop.IOLoop.current()
io_loop.clear_current()
