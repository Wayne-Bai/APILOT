import tornado.ioloop
import tornado.web

# Create a new IOLoop instance
ioloop = tornado.ioloop.IOLoop.current()

# Start the IOLoop (this makes the current thread be the IOLoop)
ioloop.start()
