import tornado.ioloop
import tornado.gen

def clear_io_loop():
    """Clears the IOLoop for the current thread."""
    # Get the current IOLoop
    io_loop = tornado.ioloop.IOLoop.current()

    # Stop the IOLoop
    io_loop.stop()

    # Wait for the IOLoop to stop
    io_loop.wait()
