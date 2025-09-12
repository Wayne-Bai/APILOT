import tornado.web
import tornado.ioloop

def make_app():
    return tornado.web.Application([])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)  # replace 8888 with your desired port number
    tornado.ioloop.IOLoop.current().start()
