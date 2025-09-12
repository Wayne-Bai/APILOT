
import tornado.ioloop

def delayed_callback(callback):
    tornado.ioloop.IOLoop.current().call_later(0, callback)

# Example usage
def callback_function():
    print("Callback was called")

delayed_callback(callback_function)

tornado.ioloop.IOLoop.current().start()
