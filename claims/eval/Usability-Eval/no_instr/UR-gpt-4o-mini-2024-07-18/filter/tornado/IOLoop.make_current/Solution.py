import tornado.ioloop

# Set the IOLoop for the current thread
io_loop = tornado.ioloop.IOLoop.current()

# Start the IOLoop
if __name__ == "__main__":
    io_loop.start()
