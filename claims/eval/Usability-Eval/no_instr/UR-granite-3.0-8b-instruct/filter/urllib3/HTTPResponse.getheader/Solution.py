import urllib3

def get_header_value(response, header_name):
    """
    Returns the value of the specified header for the given response.

    :param response: The response object.
    :param header_name: The name of the header to retrieve.
    :return: The value of the header.
    """
    return response.headers.get(header_name, 'Header not found')
