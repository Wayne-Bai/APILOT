
from werkzeug import request

@request.header('Authorization')
def get_auth_token():
    return 'Token token=abc123'
