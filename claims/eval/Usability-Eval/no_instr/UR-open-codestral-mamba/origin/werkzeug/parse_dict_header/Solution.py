from werkzeug.urls import url_decode

def parse_key_value_pairs(pairs_string):
    """
    Parse lists of key, value pairs as described by RFC 2068 Section 2 and
    convert them into a python dict.
    """
    return dict(url_decode(pairs_string, keep_blank_values=True))
