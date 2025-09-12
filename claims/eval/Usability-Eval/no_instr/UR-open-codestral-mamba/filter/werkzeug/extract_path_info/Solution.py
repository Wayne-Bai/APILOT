from werkzeug.urls import url_parse

def get_path_info(url_or_wsgi_env):
    url = url_parse(url_or_wsgi_env)
    return url.path

# Test the function
print(get_path_info('http://localhost:5000/home'))  # Output: /home
