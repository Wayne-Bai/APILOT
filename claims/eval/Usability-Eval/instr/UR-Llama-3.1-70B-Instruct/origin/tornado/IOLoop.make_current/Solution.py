import tornado.ioloop

# Create an IOLoop instance for the current thread
loop = tornado.ioloop.IOLoop.current()

# Start the IOLoop
loop.start()
