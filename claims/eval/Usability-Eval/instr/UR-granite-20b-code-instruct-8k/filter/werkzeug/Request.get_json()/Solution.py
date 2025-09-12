
from werkzeug.wrappers import Request
from werkzeug.serving import run_simple
import json

@Request.application
def application(request):
    if request.method == 'POST':
        data = request.get_json()
        return json.dumps(data)

if __name__ == '__main__':
    run_simple('localhost', 4000, application)
