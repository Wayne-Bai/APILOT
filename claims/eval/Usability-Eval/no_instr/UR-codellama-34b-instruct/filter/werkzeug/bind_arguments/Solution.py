from werkzeug.wrappers import Request, Response

def my_function(request):
    args = request.args
    return {"key1": args["value1"], "key2": args["value2"]}

@Request.application
def app(request):
    response = Response()
    data = my_function(request)
    response.data = json.dumps(data)
    return response
