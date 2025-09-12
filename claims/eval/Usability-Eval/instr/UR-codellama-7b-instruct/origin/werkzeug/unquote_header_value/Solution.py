from flask import request, Response
from werkzeug.datastructures import Headers

app = Flask(__name__)

@app.route('/')
def index():
    headers = Headers(request.headers)
    user_agent = headers['user-agent']
    unquoted_user_agent = headers.unquote(user_agent)
    return Response(str(unquoted_user_agent))
