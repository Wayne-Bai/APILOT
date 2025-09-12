from werkzeug import Request

def get_script_name():
    request = Request('http://localhost:5000')  # replace with your URL
    script_name = request.path.lstrip('/')
    return script_name

print(get_script_name())
