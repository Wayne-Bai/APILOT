from werkzeug.wrappers import Request

@Request.application
def application(request):
    return request.args.to_dict()
