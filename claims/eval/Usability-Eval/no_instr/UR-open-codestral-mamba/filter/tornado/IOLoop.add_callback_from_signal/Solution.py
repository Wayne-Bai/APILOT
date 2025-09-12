import tornado.ioloop

def callback():
    print("This is the callback function, it will be executed on the next I/O loop iteration.")

# Create a Tornado IOLoop instance
ioloop = tornado.ioloop.IOLoop.current()

# Schedule the callback to be called on the next I/O loop iteration
ioloop.add_callback(callback)

# Start the IOLoop
ioloop.start()
