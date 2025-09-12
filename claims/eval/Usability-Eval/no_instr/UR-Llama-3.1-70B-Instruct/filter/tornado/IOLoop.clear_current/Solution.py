import tornado.ioloop

# Create a new IOLoop instance
loop = tornado.ioloop.IOLoop.current()

# Clears the IOLoop for the current thread.
loop.clear_current()

print("IOLoop cleared for the current thread.")
