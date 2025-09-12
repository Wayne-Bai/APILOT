import urllib3

def get_response(request):
    http = urllib3.PoolManager()
    response = http.request('GET', request.url)
    return response
