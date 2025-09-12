
import tornado.ioloop

def callback():
    # Your code to be executed on the next I/O loop iteration goes here
    pass

tornado.ioloop.add_callback(callback)
