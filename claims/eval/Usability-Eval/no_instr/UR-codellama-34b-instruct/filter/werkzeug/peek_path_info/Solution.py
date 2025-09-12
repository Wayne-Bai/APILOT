from werkzeug.urls import url_parse, url_decode

def get_next_segment(path):
    parsed = url_parse(path)
    segments = url_decode(parsed.path)
    if len(segments) > 1:
        return segments[1]
    else:
        return None
