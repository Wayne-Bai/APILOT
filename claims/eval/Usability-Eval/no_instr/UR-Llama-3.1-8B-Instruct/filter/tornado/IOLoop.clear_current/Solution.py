import tornado.ioloop

def clear_ioloop():
    """
    Clears the IOLoop for the current thread.
    """
    io_loop = tornado.ioloop.IOLoop.instance()
    if io_loop:
        io_loop.stop()
        io_loop.close()
    else:
        print("No IOLoop instance found.")

# Usage
clear_ioloop()
tornado.ioloop.IOLoop.current().start()
