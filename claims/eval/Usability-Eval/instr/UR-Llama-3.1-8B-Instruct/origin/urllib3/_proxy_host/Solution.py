from http import client

def proxy_pass(host, port):
    try:
        http_connection = client.HTTPConnection(host, port)
        http_connection.request('GET', '/')
        response = http_connection.getresponse()
        print('Status: ', response.status)
        print('Reason: ', response.reason)
    except client.HTTPException as e:
        print('HTTP error occurred: %s' % e)
    except Exception as e:
        print('Other error occurred.')

proxy_pass('example.com', 8080)
