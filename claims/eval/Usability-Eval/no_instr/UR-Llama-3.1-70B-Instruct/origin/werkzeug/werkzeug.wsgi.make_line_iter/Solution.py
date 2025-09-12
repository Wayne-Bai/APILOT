from werkzeug.utils import safe_join
from werkzeug.wrappers import Request
from werkzeug.formparser import parse_form_stream

def safe_iterate_lines(stream):
    """
    Safely iterates line-based over an input stream.

    :param stream: The input stream to iterate over.
    :return: A generator yielding lines from the stream.
    """
    yield from stream.iter_encoded(minsize=1024, maxsize=65536)


class CustomRequest(Request):
    def get_stream(self):
        """
        Returns the input stream for the current request.

        :return: The input stream.
        """
        return self.environ['wsgi.input']


def handle_request(environ, start_response):
    """
    A basic WSGI application that demonstrates the safe iteration.

    :param environ: The WSGI environment.
    :param start_response: The WSGI start response callback.
    """
    request = CustomRequest(environ)

    # Parse the input data as form/multipart
    data = parse_form_stream(request)

    for key, value in data:
        print(f"Key: {key}, Value: {value}")

    stream = request.get_stream()
    for line in safe_iterate_lines(stream):
        print(f"Received line: {line}")

    start_response('200 OK', [])
    return ['Hello, World!']
