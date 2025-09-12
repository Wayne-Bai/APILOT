import tornado.ioloop
import tornado.web

def callback():
    print("Callback called!")

# Register the function to be called after the current I/O loop iteration
tornado.ioloop.IOLoop.current().add_callback(callback)

# Keep the I/O loop running
tornado.ioloop.IOLoop.current().start()
