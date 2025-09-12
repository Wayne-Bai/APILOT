
import tornado.ioloop

# Create a new IOLoop instance
loop = tornado.ioloop.IOLoop()

# Set the loop as the default loop for the current thread
tornado.ioloop.IOLoop.set_default(loop)
