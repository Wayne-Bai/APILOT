import tornado.ioloop
import functools

def call_on_next_iteration(callback):
    tornado.ioloop.IOLoop.current().add_callback(callback)

# Example usage:
def my_callback():
    print("Callback was called")

call_on_next_iteration(my_callback)
