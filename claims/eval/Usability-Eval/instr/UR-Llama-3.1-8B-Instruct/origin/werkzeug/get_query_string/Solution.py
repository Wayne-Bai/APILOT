# Import the required modules
from werkzeug.datastructures import ImmutableMultiDict

# Function to get the QUERY_STRING from the WSGI environment
def get_query_string(environ):
    """
    Returns the QUERY_STRING from the WSGI environment.

    Args:
        environ (dict): The WSGI environment.

    Returns:
        str: The QUERY_STRING value.
    """
    # Get the QUERY_STRING from the environ dictionary
    query_string = environ.get('QUERY_STRING')
    
    # Return the QUERY_STRING
    return query_string

# Example usage
environ = {
    'QUERY_STRING': 'key=value&foo=bar'
}

print(get_query_string(environ))  # Output: 'key=value&foo=bar'
