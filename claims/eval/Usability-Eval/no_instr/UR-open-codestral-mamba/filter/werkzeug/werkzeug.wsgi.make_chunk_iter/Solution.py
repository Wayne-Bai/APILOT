from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    def custom_line_iter(separator):
        content_length = int(request.headers.get('Content-Length', 0))
        remaining_bytes = content_length
        buffered = b''
        while remaining_bytes > 0:
            part = request.stream.read(remaining_bytes)
            if not part:  # end of stream
                break
            buffered += part
            while True:  # split chunk on separator
                chunk, separator, buffered = buffered.partition(separator.encode())
                if not chunk:
                    break
                remaining_bytes -= len(chunk) + len(separator)
                yield chunk
    separator = request.args.get('sep', '\n')  # use newline as default separator
    response = Response(custom_line_iter(separator))
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'  # e.g., for text files
    return response
