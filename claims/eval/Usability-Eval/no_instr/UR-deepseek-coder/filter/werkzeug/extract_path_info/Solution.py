from werkzeug.routing import Map, Rule

def extract_path_info(url_or_environ):
    # Create a URL map
    url_map = Map([
        Rule('/<path:path>', endpoint='path_info')
    ])

    # Match the URL or WSGI environment
    if isinstance(url_or_environ, str):
        adapter = url_map.bind('example.com')
        match = adapter.match(url_or_environ)
    else:
        adapter = url_map.bind_to_environ(url_or_environ)
        match = adapter.match()

    # Extract the path info
    path_info = match.get('path', '')
    return path_info

# Example usage:
url = '/some/path/info'
environ = {
    'wsgi.url_scheme': 'http',
    'HTTP_HOST': 'example.com',
    'PATH_INFO': '/some/path/info'
}

print(extract_path_info(url))        # Output: some/path/info
print(extract_path_info(environ))    # Output: some/path/info
