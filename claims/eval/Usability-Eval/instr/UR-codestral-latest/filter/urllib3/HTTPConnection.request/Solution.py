import urllib3

def send_request(url, method):
    http = urllib3.PoolManager()

    if method == "GET":
        response = http.request('GET', url)
    elif method == "POST":
        response = http.request('POST', url, fields={'key': 'value'})
    else:
        print("Unsupported method")
        return

    print('Response status: ', response.status)
    print('Response data: ', response.data)

# example usage
send_request('http://example.com/some_url', 'GET')
