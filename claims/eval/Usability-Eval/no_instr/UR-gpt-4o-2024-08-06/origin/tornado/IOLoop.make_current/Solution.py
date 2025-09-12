import tornado.ioloop

def main():
    # Get the current IOLoop instance, or create one if it doesn't exist
    io_loop = tornado.ioloop.IOLoop.current()

    # Make this the IOLoop for the current thread
    io_loop.make_current()

    # Start the IOLoop
    io_loop.start()

if __name__ == "__main__":
    main()
