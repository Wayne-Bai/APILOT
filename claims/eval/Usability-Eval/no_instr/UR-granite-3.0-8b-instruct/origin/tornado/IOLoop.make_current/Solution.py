import tornado.ioloop

# Make this the IOLoop for the current thread
tornado.ioloop.Current.instance().start()
