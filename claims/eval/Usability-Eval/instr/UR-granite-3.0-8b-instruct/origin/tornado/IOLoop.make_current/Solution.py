import tornado.ioloop

# Make this the IOLoop for the current thread.
tornado.ioloop.IOLoop.current().make_current()
