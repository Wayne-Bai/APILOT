import tornado.ioloop

if __name__ == "__main__":
    # Set up the IOLoop for the current thread
    io_loop = tornado.ioloop.IOLoop.current()
    
    # Start the IOLoop
    io_loop.start()
