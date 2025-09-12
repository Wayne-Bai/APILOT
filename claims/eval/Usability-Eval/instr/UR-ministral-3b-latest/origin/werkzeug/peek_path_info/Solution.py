from werkzeug import Request

request = Request()
segment = request.args.get('REQUEST_SEGMENT')

if segment is None:
    segment = request.path_info
