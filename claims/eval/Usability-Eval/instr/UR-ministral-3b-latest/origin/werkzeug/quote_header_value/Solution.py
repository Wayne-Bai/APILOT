from werkzeug.wrappers import Request, Response

def printHeaderValue(request):
    if request.headers.get('X-Test-Header') is None:
        request.headers['X-Test-Header'] = 'Quote header value'
    print(request.headers['X-Test-Header'])

def testApp():
    request = Request.blank('https://example.com', headers={'X-Test-Header': 'some-header-value'})
    printHeaderValue(request)
    response = Response('Test')
    return Response(response, request)

if __name__ == '__main__':
    testApp()
