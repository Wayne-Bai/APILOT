import tornado.ioloop

def callback_function():
    print("Callback function called on the next I/O loop iteration.")

def main():
    # Get the current I/O loop instance
    io_loop = tornado.ioloop.IOLoop.current()
    
    # Call the callback function on the next I/O loop iteration
    io_loop.call_soon(callback_function)
    
    # Start the I/O loop
    io_loop.start()

if __name__ == "__main__":
    main()
