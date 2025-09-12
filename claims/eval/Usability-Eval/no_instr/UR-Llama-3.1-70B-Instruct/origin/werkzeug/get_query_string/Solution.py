from werkzeug import Request
from werkzeug.local import LocalProxy

def get_query_string():
    """
    Returns the `QUERY_STRING` from the WSGI environment.
    """
    environ = Request.environ
    return environ.get('QUERY_STRING')

# Example usage
if __name__ == "__main__":
    # Define the WSGI environment variables
    class MockEnviron(object):
        def __init__(self, query_string):
            self.QUERY_STRING = query_string

    # Create a mock WSGI environment
    query_string = "name=John+Doe&age=30"
    environ = MockEnviron(query_string)

    # Set the WSGI environment for this request
    Request.environ = environ

    query_string_value = get_query_string()
    print("QUERY_STRING:", query_string_value)

    # Output: QUERY_STRING: name=John+Doe&age=30
