import tornado.ioloop

def clear_ioloop():
    """
    Clears the IOLoop for the current thread.
    """
    loop = tornado.ioloop.IOLoop.current()
    if loop is not None:
        loop.clear()

# Usage:
if __name__ == "__main__":
    # Create an instance of IOLoop
    loop = tornado.ioloop.IOLoop.current()
    
    # Start the IOLoop
    loop.start()
    
    # Clear the IOLoop
    clear_ioloop()

    # Check if IOLoop is cleared
    if tornado.ioloop.IOLoop.current() is None:
        print("IOLoop has been cleared")
    else:
        print("IOLoop has not been cleared")
