import werkzeug
class HTTPException(Exception):
    code = 500
    description = 'Internal Server Error'
class InternalServerError(HTTPException, werkzeug.HTTPException):
    pass
