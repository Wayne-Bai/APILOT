from werkzeug.wrappers import Request

def make_chunk_iter(stream, separator):
    temp = b''
    for chunk in stream:
        temp += chunk
        while separator in temp:
            idx = temp.index(separator)
            yield temp[:idx]
            temp = temp[idx + len(separator):]
    yield temp

@Request.application
def application(request):
    return '\n'.join(make_chunk_iter(request.stream, b'\n'))
