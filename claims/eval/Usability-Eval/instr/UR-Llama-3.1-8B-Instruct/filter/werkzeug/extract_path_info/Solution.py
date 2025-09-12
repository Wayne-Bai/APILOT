from werkzeug import routing

def extract_path_info(url=None, wsgi_environment={}):
    """
    Extracts the path info from the given URL or WSGI environment.

    Args:
        url (str, optional): The URL to extract path info from. Defaults to None.
        wsgi_environment (dict, optional): The WSGI environment to extract path info from. Defaults to {}.

    Returns:
        str: The path info extracted from the URL or WSGI environment.
    """
    
    # Create a BaseConverter instance that can be used to handle URLs
    converter = routing.BaseConverter('/')
    
    # If a URL is provided, use the URL Hague rules to extract the path info
    if url:
        return converter.map(
            *url.split('/')[1:], 
            strict_slash=False
        )
    
    # If a WSGI environment is provided, check for PATH_INFO key
    elif 'PATH_INFO' in wsgi_environment:
        # The PATH_INFO key in the WSGI environment contains the path info
        return wsgi_environment['PATH_INFO']
    
    # If neither a URL nor a WSGI environment is provided, return an empty string
    else:
        return ''

# Test the function
url = '/users/john'
wsgi_environment = {'PATH_INFO': '/stats/top'}
print(extract_path_info(url))  # Output: users/john
print(extract_path_info(wsgi_environment={'PATH_INFO': '/stats/top'}))  # Output: stats/top
print(extract_path_info())  # Output: ''
