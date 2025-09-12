from werkzeug.wrappers import Request

@Request.application
def application(request):
    # All the arguments are stored in request.args
    args = request.args.to_dict()

    return process_args(args)

def process_args(args):
    # Your function to process the arguments
    pass
