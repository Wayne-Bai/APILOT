from werkzeug import parse_qs

def parse_query_string(query_string):
    return dict(parse_qs(query_string))
