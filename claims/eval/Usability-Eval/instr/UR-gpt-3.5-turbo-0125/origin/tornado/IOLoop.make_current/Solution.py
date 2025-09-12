
import tornado.ioloop

def make_current_ioloop():
    ioloop_instance = tornado.ioloop.IOLoop.current()
    return ioloop_instance

if __name__ == "__main__":
    current_ioloop = make_current_ioloop()
    print("Current IOLoop for the thread:", current_ioloop)
