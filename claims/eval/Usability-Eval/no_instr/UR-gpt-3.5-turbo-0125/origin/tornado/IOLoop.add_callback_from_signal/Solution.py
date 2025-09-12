
import tornado.ioloop

def callback():
    print("Callback called on the next I/O loop iteration")

tornado.ioloop.IOLoop.current().add_callback(callback)
tornado.ioloop.IOLoop.current().start()
