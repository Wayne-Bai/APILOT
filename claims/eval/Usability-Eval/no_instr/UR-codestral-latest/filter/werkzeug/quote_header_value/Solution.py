from werkzeug.wrappers import Request, Response
from urllib.parse import quote, unquote

@Request.application
def application(request):
    header_value = request.headers.get('My-Header')

    if header_value:
        # If the header value contains any character which is not allowed in HTTP headers,
        # quote the value to make it valid.
        if not all(c.isalnum() or c in '!#$%&\'()*+-./:<=>?@[]^_`{|}~' for c in header_value):
            header_value = quote(header_value)

    # Rest of your code...
