from werkzeug.urls import url_parse

def extract_path_info(url):
    parsed_url = url_parse(url)
    return parsed_url.path
