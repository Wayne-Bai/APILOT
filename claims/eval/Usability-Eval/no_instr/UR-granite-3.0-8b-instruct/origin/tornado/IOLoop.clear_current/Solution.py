import tornado.ioloop

def clear_ioloop():
    # Clear the IOLoop for the current thread
    tornado.ioloop.IOLoop.clear_instance()

# Usage
clear_ioloop()
