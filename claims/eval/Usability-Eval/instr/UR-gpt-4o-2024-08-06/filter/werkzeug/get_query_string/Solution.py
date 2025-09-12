from werkzeug.wrappers import Request

@Request.application
def application(request):
    query_string = request.query_string.decode('utf-8')  # Get the QUERY_STRING from the WSGI environment
    return Response(f"The query string is: {query_string}", mimetype='text/plain')

# To run this application, you would need a WSGI server, for example, using Werkzeug's built-in server:
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)
