from werkzeug import urls

# This is an example URL
url = "http://example.com/users/123/orders?page=2"

# To extract the path info from a given URL
path_info = urls.urlparse(url)._path

print("Path info from the URL:", path_info)

# To extract the path info from a WSGI environment dictionary
wsgi_environment = {
    "PATH_INFO": "/users/123/orders",
    "QUERY_STRING": "page=2",
    "SCRIPT_NAME": "",
    "SERVER_NAME": "example.com",
    "SERVER_PORT": "80",
    "SERVER_PROTOCOL": "HTTP/1.1"
}

# Werkzeug does not provide a direct method to get the path info from the WSGI environment
# However, we can use the url_join function to construct the full URL from the path info and other variables.
# Here, we use urls.url_join function to construct the full URL, then use urls.urlparse to get the path info.
import urllib.parse

path_info = urllib.parse.urlparse(urls.url_join(wsgi_environment['SCRIPT_NAME'], wsgi_environment['PATH_INFO']))

print("Path info from the WSGI environment:", path_info.path)
