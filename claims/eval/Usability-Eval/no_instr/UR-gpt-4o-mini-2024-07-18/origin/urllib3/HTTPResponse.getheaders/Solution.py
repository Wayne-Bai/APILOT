import urllib3

class UnmodifiableHeaders:
    def __init__(self, headers):
        self._headers = headers

    def get_headers(self):
        return {key: value for key, value in self._headers.items()}

    def __getitem__(self, key):
        return self._headers[key]

    def __iter__(self):
        return iter(self._headers)

    def __len__(self):
        return len(self._headers)

http = urllib3.PoolManager()
response = http.request('GET', 'http://httpbin.org/headers')

unmodifiable_headers = UnmodifiableHeaders(response.headers)

# Example usage
print("HTTP Headers:")
for key, value in unmodifiable_headers.get_headers().items():
    print(f"{key}: {value}")
