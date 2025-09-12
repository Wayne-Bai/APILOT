import tornado.ioloop
import tornado.gen

def call_in_ioloop(callback):
    """
    Calls the given callback on the next I/O loop iteration.
    """
    tornado.ioloop.IOLoop.current().add_callback(callback)

# Example usage:
def my_callback():
    print("Callback called in I/O loop.")

call_in_ioloop(my_callback)
