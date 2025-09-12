import tornado.web

def set_header(response, header_name, header_value):
    response.set_header(header_name, str(header_value))
