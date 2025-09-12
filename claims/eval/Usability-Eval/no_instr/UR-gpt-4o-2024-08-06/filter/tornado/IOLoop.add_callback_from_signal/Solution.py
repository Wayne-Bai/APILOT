import tornado.ioloop

def my_callback():
    print("Callback is called on the next I/O loop iteration")

# Get the current I/O loop
io_loop = tornado.ioloop.IOLoop.current()

# Add the callback to be executed on the next iteration of the I/O loop
io_loop.add_callback(my_callback)

# Start the I/O loop
io_loop.start()
