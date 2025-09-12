import tornado.ioloop

def callback_function():
    print("Callback function called!")

# Schedule the callback to be called on the next I/O loop iteration
tornado.ioloop.IOLoop.current().add_callback(callback_function)

# Start the I/O loop
tornado.ioloop.IOLoop.current().start()
