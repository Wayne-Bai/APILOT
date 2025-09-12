
from tornado import web

app = web.Application([])

if __name__ == "__main__":
    app.listen(8080)
    print("Server is listening on port 8080")
    print("Press Ctrl+C to stop the server")
