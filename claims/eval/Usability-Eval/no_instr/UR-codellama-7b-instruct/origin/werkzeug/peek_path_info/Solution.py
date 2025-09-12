from werkzeug.urls import url_parse

def get_next_segment(url):
    parsed = url_parse(url)
    if len(parsed.path) >= 2:
        return parsed.path[1]
    else:
        return None
