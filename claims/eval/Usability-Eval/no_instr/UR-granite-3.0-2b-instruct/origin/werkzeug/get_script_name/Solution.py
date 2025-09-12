from werkzeug import Request

def get_script_name():
    request = Request.dummy()
    request.path = '/path/to/your/resource'
    return request.path.decode('utf-8')

print(get_script_name())
