from urllib3 import HTTPConnection

def get_headers(connection):
    headers = connection.get_headers()
    return headers

# Example usage:
connection = HTTPConnection("www.example.com")
headers = get_headers(connection)
for key, value in headers.items():
    print(f"{key}: {value}")
