import urllib3

# Create a connection pool
http = urllib3.PoolManager()

class AppEngineConnectionManager:
    def __init__(self):
        self.http = http

    def request(self, method, url, headers=None, data=None, params=None):
        if method.upper() not in ['GET', 'POST']:
            raise ValueError(f"Unsupported HTTP method: {method}")

        enc = urllib3.utilEncoders.encode_body_parameters
        if params:
            params = enc(params)

        req = self.http.request(
            method.upper(),
            url,
            headers=headers or {},
            body=data or '',
            params=params
        )

        return req

if __name__ == '__main__':
    # Example usage
    connection_manager = AppEngineConnectionManager()
    response = connection_manager.request('GET', 'https://www.example.com')
    print(response.data)
