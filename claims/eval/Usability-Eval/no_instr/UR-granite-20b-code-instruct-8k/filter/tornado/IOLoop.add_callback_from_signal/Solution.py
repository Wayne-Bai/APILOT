
import tornado
from tornado.ioloop import IOLoop

def callback():
    print("Callback called")

IOLoop.current().add_callback(callback)
IOLoop.current().start()
