import tornado.ioloop

def main():
    print("Starting IOLoop")
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
