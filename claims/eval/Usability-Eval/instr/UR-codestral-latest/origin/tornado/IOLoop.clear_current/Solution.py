import tornado.ioloop

# Get the current IOLoop instance
ioloop = tornado.ioloop.IOLoop.current()

# Clear all callbacks from the IOLoop's instance
ioloop.clear_current()
