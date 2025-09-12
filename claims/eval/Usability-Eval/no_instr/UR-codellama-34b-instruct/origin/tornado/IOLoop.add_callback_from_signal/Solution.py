
import tornado.ioloop

def my_callback():
    print("Hello from Tornado!")

tornado.ioloop.IOLoop.current().add_timeout(time.time() + 1, my_callback)
