import tornado.ioloop

# Clear the IOLoop for the current thread
tornado.ioloop.IOLoop.current().run_until_complete(tornado.ioloop.sleep(0))

# To start the IOLoop again
tornado.ioloop.IOLoop.current().run()
