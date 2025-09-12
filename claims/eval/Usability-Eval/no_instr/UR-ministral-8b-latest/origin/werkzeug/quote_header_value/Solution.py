import werkzeug
from werkzeug.wrappers import Request

def quote_header_value(request):
    headers = request.headers
    quoted_value = werkzeug._quote(headers['Content-Type'])  # replace 'Content-Type' with the desired header key
    return quoted_value

# Example usage:
# request = Request(consumer, '/home', methodOverrides={'GET': 'POST'}, env={'HTTP_CONNECTION': 'keep-alive'})
# quote_header_value(request)
