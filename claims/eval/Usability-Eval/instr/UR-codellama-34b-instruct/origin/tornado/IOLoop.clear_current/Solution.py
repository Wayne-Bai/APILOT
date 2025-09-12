import tornado.ioloop

# Create an IOLoop instance
ioloop = tornado.ioloop.IOLoop()

# Clear the IOLoop for the current thread
ioloop.clear_current()
