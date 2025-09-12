import tornado.ioloop
import tornado.concurrent

def call_next_loop(callback):
    """
    Calls the given callback on the next I/O loop iteration.
    """
    future = tornado.concurrent.Future()
    io_loop = tornado.ioloop.IOLoop.current()
    def _call_next_loop():
        def wrap_callback():
            io_loop.stop()  # Ensure _call_next_loop is never called again
            try:
                future.set_result(callback())
            except Exception as e:
                future.set_exception(e)
        next_loop_time = io_loop.time() + 0.0001  # Schedule _call_next_loop for the next I/O loop iteration
        io_loop.add_timeout(next_loop_time, wrap_callback)
    io_loop.add_callback(_call_next_loop)

# Example usage:
def my_callback():
    print("Example callback")

call_next_loop(my_callback)
tornado.ioloop.IOLoop.current().start()
