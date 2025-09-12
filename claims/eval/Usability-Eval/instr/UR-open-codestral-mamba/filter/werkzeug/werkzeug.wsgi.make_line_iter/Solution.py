from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    @request.stream_with_context
    def generate():
        for line in request.input_stream:
            yield line
    return Response(generate(), mimetype='text/plain')
