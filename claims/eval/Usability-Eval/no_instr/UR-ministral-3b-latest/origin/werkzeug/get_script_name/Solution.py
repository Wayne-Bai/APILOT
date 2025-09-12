from werkzeug import WSGIApplication, request

# Assuming `app` is your WSGI application
app = WSGIApplication([...])  # your route definitions here

@app.before_request
def before_request():
    script_name = request.environ.get('WSGI\RequestSCRIPTNAME')
    if script_name:
        request.script_name = request.script_name or ""
        request.environ['WSGI.RequestSCRIPTNAME'] = script_name.decode('utf-8') if isinstance(request.script_name, bytes) else script_name
    else:
        request.environ['SCRIPT_NAME'] = ""

def decode_script_name(script_name):
    return script_name.encode('utf-8') if isinstance(script_name, str) else script_name

@app.route('/')
def index():
    print("SCRIPT_NAME:", decode_script_name(request.environ.get('SCRIPT_NAME', '')))
    return "Hello, World!"
