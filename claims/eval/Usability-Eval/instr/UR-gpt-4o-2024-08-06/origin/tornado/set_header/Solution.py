import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Set response header 'Custom-Header' to 'MyValue'
        self.add_header('Custom-Header', str('MyValue'))
        
        # Set response header 'Another-Header' to an integer value converted to string
        self.add_header('Another-Header', str(12345))
        
        # Write a response
        self.write("Headers have been set!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
