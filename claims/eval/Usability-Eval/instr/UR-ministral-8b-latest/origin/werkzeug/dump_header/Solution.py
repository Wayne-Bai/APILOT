from werkzeug.wrappers import Response

app = Response('data', mimetype='text/html')

def dump_header():
    return app.streaming_headers

# Example usage
if __name__ == "__main__":
    headers = dump_header()
    for key, value in headers.items():
        print(f"{key}: {value}")
