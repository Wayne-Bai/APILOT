from werkzeug import local

# Define a custom request object to access the environment
request = local.LocalProxy(lambda: local.request)

# Function to return the QUERY_STRING from the WSGI environment
def get_query_string():
    """
    Returns the QUERY_STRING from the WSGI environment.

    Returns:
        str: The query string.
    """
    return request.args

# Example usage:
print(get_query_string())
