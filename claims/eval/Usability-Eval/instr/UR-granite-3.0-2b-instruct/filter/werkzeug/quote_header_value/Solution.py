from werkzeug import ln

def quote_header(header):
    return ln(header).replace("\"", "\\\"")
