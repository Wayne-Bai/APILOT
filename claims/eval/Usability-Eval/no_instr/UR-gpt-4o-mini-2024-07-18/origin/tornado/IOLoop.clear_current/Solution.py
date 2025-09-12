import tornado.ioloop

def main():
    # Clear the IOLoop for the current thread
    tornado.ioloop.IOLoop.current().clear_current()

if __name__ == "__main__":
    main()
