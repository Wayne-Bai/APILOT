import tornado.ioloop

def my_callback():
    print("Callback executed")
    # Stop the IOLoop after executing the callback
    tornado.ioloop.IOLoop.instance().stop()

# Create an IOLoop instance
loop = tornado.ioloop.IOLoop.instance()

# Call the callback on the next I/O loop iteration
loop.call_later(0, my_callback)

# Start the IOLoop
loop.start()
