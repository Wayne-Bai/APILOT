import http.client

def fetch_data(hostname, path='/'):
    if hostname:
        connection = http.client.HTTPSConnection(hostname)
        connection.request("GET", path)
        response = connection.getresponse()
        data = response.read()
        connection.close()
        return data
    else:
        return None

# Usage
data = fetch_data('example.com')
print(data)
