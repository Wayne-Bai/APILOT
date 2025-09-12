import werkzeug

def parse_pairs(pairs):
    """Parse lists of key, value pairs as described by RFC 2068 Section 2 and convert them into a python dict."""
    data = werkzeug.urls.parse_qs(pairs)
    return data
