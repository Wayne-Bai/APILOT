import tornado.ioloop

def my_callback():
    print("Callback is called")

# Create an instance of IOLoop
io_loop = tornado.ioloop.IOLoop.current()

# Call the callback on the next I/O loop iteration
io_loop.add_callback(my_callback)

# Start the IOLoop
io_loop.start()
