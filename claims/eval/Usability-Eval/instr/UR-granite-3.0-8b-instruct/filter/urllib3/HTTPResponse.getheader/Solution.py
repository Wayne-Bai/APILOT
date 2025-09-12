from urllib3.response import HTTPResponse

def get_header_value(response, header_name):
    """
    Returns the value of the specified header for the given response.

    :param response: The HTTP response object.
    :param header_name: The name of the header to retrieve.
    :return: The value of the specified header.
    """
    return response.headers.get(header_name)
