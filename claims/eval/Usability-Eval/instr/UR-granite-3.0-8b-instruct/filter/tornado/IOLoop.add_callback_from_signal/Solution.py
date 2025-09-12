import tornado.ioloop
import tornado.gen

def call_callback():
    # Your callback code here
    pass

def main():
    tornado.ioloop.IOLoop.current().add_callback(call_callback)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
