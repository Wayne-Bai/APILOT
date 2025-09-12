import tornado.ioloop

def making_it_live():
    print("Loop is running")

# create the ioloop
ioloop = tornado.ioloop.IOLoop.current()

# add a task and start the ioloop
ioloop.add_callback(making_it_live)
ioloop.start()

