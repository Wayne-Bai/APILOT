from urllib3.poolmanager import PoolManager

def get_connection_and_request(url, headers, params, data, timeout):
    pm = PoolManager(maxsize=10)
    connection = pm.get_connection(timeout=timeout)

    # Create a Request object with only the request-uri portion of the URL
    request = urllib3.Request(url, headers=headers, params=params, data=data, timeout=timeout)
    request.connect_timeout = timeout

    # Send the request and get the response
    response = connection.request(request).getresponse()

    return response
