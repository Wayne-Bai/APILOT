import tornado.ioloop

def my_callback():
    print("Callback executed!")

# Call the callback on the next I/O loop iteration
tornado.ioloop.IOLoop.current().call_later(0, my_callback)

# Start the I/O loop
tornado.ioloop.IOLoop.current().start()
