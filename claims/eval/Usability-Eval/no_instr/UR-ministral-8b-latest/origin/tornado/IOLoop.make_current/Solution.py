import tornado.ioloop

# Create a new IOLoop in the current thread
current_ioloop = tornado.ioloop.IOLoop.current()

# Example of an asynchronous function
def asynchronous_function():
    # This will be scheduled to run asynchronously
    print("Task started!")

# Schedule the function to run in the current IOLoop
current_ioloop.add_callback(asynchronous_function)

# Start the IOLoop in the current thread
current_ioloop.start()
